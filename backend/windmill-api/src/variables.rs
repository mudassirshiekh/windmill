/*
 * Author: Ruben Fiszel
 * Copyright: Windmill Labs, Inc 2022
 * This file and its contents are licensed under the AGPLv3 License.
 * Please see the included NOTICE for copyright information and
 * LICENSE-AGPL for a copy of the license.
 */

use crate::{
    db::{ApiAuthed, DB},
    oauth2::_refresh_token,
    users::{maybe_refresh_folders, require_owner_of_path},
    webhook_util::{WebhookMessage, WebhookShared},
};

use axum::{
    extract::{Extension, Path, Query},
    routing::{delete, get, post},
    Json, Router,
};
use hyper::StatusCode;
use serde_json::Value;
use windmill_audit::{audit_log, ActionKind};
use windmill_common::{
    db::UserDB,
    error::{Error, JsonResult, Result},
    utils::{not_found_if_none, StripPath},
    variables::{get_reserved_variables, ContextualVariable, CreateVariable, ListableVariable},
};

use lazy_static::lazy_static;
use magic_crypt::{MagicCrypt256, MagicCryptTrait};
use serde::Deserialize;
use sqlx::{Postgres, Transaction};

lazy_static! {
    pub static ref SECRET_SALT: Option<String> = std::env::var("SECRET_SALT").ok();
}

pub fn workspaced_service() -> Router {
    Router::new()
        .route("/list", get(list_variables))
        .route("/list_contextual", get(list_contextual_variables))
        .route("/get/*path", get(get_variable))
        .route("/get_value/*path", get(get_value))
        .route("/exists/*path", get(exists_variable))
        .route("/update/*path", post(update_variable))
        .route("/delete/*path", delete(delete_variable))
        .route("/create", post(create_variable))
        .route("/encrypt", post(encrypt_value))
}

async fn list_contextual_variables(
    Path(w_id): Path<String>,
    ApiAuthed { username, email, .. }: ApiAuthed,
) -> JsonResult<Vec<ContextualVariable>> {
    Ok(Json(
        get_reserved_variables(
            &w_id,
            "q1A0qcPuO00yxioll7iph76N9CJDqn",
            &email,
            &username,
            "017e0ad5-f499-73b6-5488-92a61c5196dd",
            format!("u/{username}").as_str(),
            Some("u/user/script_path".to_string()),
            Some("017e0ad5-f499-73b6-5488-92a61c5196dd".to_string()),
            Some("u/user/encapsulating_flow_path".to_string()),
            Some("u/user/triggering_flow_path".to_string()),
            Some("c".to_string()),
        )
        .to_vec(),
    ))
}

async fn list_variables(
    authed: ApiAuthed,
    Extension(user_db): Extension<UserDB>,
    Path(w_id): Path<String>,
) -> JsonResult<Vec<ListableVariable>> {
    let mut tx = user_db.begin(&authed).await?;

    let rows = sqlx::query_as::<_, ListableVariable>(
        "SELECT variable.workspace_id, variable.path, CASE WHEN is_secret IS TRUE THEN null ELSE variable.value::text END as value, 
         is_secret, variable.description, variable.extra_perms, account, is_oauth, (now() > account.expires_at) as is_expired,
         account.refresh_error,
         resource.path IS NOT NULL as is_linked,
         account.refresh_token != '' as is_refreshed
         from variable
         LEFT JOIN account ON variable.account = account.id AND account.workspace_id = $1
         LEFT JOIN resource ON resource.path = variable.path AND resource.workspace_id = $1
         WHERE variable.workspace_id = $1 ORDER BY path",
    )
    .bind(&w_id)
    .fetch_all(&mut *tx)
    .await?;

    tx.commit().await?;
    Ok(Json(rows))
}

#[derive(Deserialize)]
struct GetVariableQuery {
    decrypt_secret: Option<bool>,
}

async fn get_variable(
    authed: ApiAuthed,
    Extension(user_db): Extension<UserDB>,
    Query(q): Query<GetVariableQuery>,
    Path((w_id, path)): Path<(String, StripPath)>,
) -> JsonResult<ListableVariable> {
    let path = path.to_path();
    let mut tx = user_db.begin(&authed).await?;

    let variable_o = sqlx::query_as::<_, ListableVariable>(
        "SELECT variable.*, (now() > account.expires_at) as is_expired, account.refresh_error,
        resource.path IS NOT NULL as is_linked,
        account.refresh_token != '' as is_refreshed
        from variable
        LEFT JOIN account ON variable.account = account.id
        LEFT JOIN resource ON resource.path = variable.path AND resource.workspace_id = $2
        WHERE variable.path = $1 AND variable.workspace_id = $2
        LIMIT 1",
    )
    .bind(&path)
    .bind(&w_id)
    .fetch_optional(&mut *tx)
    .await?;

    let variable = not_found_if_none(variable_o, "Variable", &path)?;

    let decrypt_secret = q.decrypt_secret.unwrap_or(true);

    let r = if variable.is_secret {
        if decrypt_secret {
            audit_log(
                &mut *tx,
                &authed.username,
                "variables.decrypt_secret",
                ActionKind::Execute,
                &w_id,
                Some(&variable.path),
                None,
            )
            .await?;
        }
        let value = variable.value.unwrap_or_else(|| "".to_string());
        ListableVariable {
            value: if variable.is_expired.unwrap_or(false) && variable.account.is_some() {
                Some(_refresh_token(tx, &variable.path, &w_id, variable.account.unwrap()).await?)
            } else if !value.is_empty() && decrypt_secret {
                let mc = build_crypt(&mut tx, &w_id).await?;
                tx.commit().await?;

                Some(
                    mc.decrypt_base64_to_string(value)
                        .map_err(|e| Error::InternalErr(e.to_string()))?,
                )
            } else {
                None
            },
            ..variable
        }
    } else {
        variable
    };

    Ok(Json(r))
}

async fn get_value(
    authed: ApiAuthed,
    Extension(user_db): Extension<UserDB>,
    Path((w_id, path)): Path<(String, StripPath)>,
) -> JsonResult<String> {
    let path = path.to_path();
    let tx = user_db.begin(&authed).await?;
    return get_value_internal(tx, &w_id, &path, &authed.username)
        .await
        .map(Json);
}

pub async fn get_value_internal<'c>(
    mut tx: Transaction<'c, Postgres>,
    w_id: &str,
    path: &str,
    username: &str,
) -> Result<String> {
    let variable_o = sqlx::query!(
        "SELECT value, account, (now() > account.expires_at) as is_expired, is_secret, path from variable
        LEFT JOIN account ON variable.account = account.id WHERE variable.path = $1 AND variable.workspace_id = $2", path, w_id
    )
    .fetch_optional(&mut *tx)
    .await?;

    let variable = not_found_if_none(variable_o, "Variable", &path)?;

    let r = if variable.is_secret {
        audit_log(
            &mut *tx,
            username,
            "variables.decrypt_secret",
            ActionKind::Execute,
            &w_id,
            Some(&variable.path),
            None,
        )
        .await?;
        let value = variable.value;
        if variable.is_expired.unwrap_or(false) && variable.account.is_some() {
            _refresh_token(tx, &variable.path, &w_id, variable.account.unwrap()).await?
        } else if !value.is_empty() {
            let mc = build_crypt(&mut tx, &w_id).await?;
            tx.commit().await?;

            mc.decrypt_base64_to_string(value)
                .map_err(|e| Error::InternalErr(e.to_string()))?
        } else {
            "".to_string()
        }
    } else {
        variable.value
    };

    Ok(r)
}

async fn exists_variable(
    Extension(db): Extension<DB>,
    Path((w_id, path)): Path<(String, StripPath)>,
) -> JsonResult<bool> {
    let path = path.to_path();

    let exists = sqlx::query_scalar!(
        "SELECT EXISTS(SELECT 1 FROM variable WHERE path = $1 AND workspace_id = $2)",
        path,
        w_id
    )
    .fetch_one(&db)
    .await?
    .unwrap_or(false);

    Ok(Json(exists))
}

async fn check_path_conflict<'c>(
    tx: &mut Transaction<'c, Postgres>,
    w_id: &str,
    path: &str,
) -> Result<()> {
    let exists = sqlx::query_scalar!(
        "SELECT EXISTS(SELECT 1 FROM variable WHERE path = $1 AND workspace_id = $2)",
        path,
        w_id
    )
    .fetch_one(&mut **tx)
    .await?
    .unwrap_or(false);
    if exists {
        return Err(Error::BadRequest(format!(
            "Variable {} already exists",
            path
        )));
    }
    return Ok(());
}

async fn create_variable(
    authed: ApiAuthed,
    Extension(db): Extension<DB>,
    Extension(user_db): Extension<UserDB>,
    Extension(webhook): Extension<WebhookShared>,
    Path(w_id): Path<String>,
    Query(AlreadyEncrypted { already_encrypted }): Query<AlreadyEncrypted>,
    Json(variable): Json<CreateVariable>,
) -> Result<(StatusCode, String)> {
    let authed = maybe_refresh_folders(&variable.path, &w_id, authed, &db).await;

    let mut tx = user_db.begin(&authed).await?;

    check_path_conflict(&mut tx, &w_id, &variable.path).await?;
    let value = if variable.is_secret && !already_encrypted.unwrap_or(false) {
        let mc = build_crypt(&mut tx, &w_id).await?;
        encrypt(&mc, &variable.value)
    } else {
        variable.value
    };

    sqlx::query!(
        "INSERT INTO variable
            (workspace_id, path, value, is_secret, description, account, is_oauth)
            VALUES ($1, $2, $3, $4, $5, $6, $7)",
        &w_id,
        variable.path,
        value,
        variable.is_secret,
        variable.description,
        variable.account,
        variable.is_oauth.unwrap_or(false),
    )
    .execute(&mut *tx)
    .await?;

    audit_log(
        &mut *tx,
        &authed.username,
        "variables.create",
        ActionKind::Create,
        &w_id,
        Some(&variable.path),
        None,
    )
    .await?;

    tx.commit().await?;

    webhook.send_message(
        w_id.clone(),
        WebhookMessage::CreateVariable { workspace: w_id, path: variable.path.clone() },
    );

    Ok((
        StatusCode::CREATED,
        format!("variable {} created", variable.path),
    ))
}

async fn encrypt_value(
    Extension(db): Extension<DB>,
    Path(w_id): Path<String>,
    Json(variable): Json<String>,
) -> Result<String> {
    let mut tx = db.begin().await?;

    let mc = build_crypt(&mut tx, &w_id).await?;
    let value = encrypt(&mc, &variable);

    tx.commit().await?;

    Ok(value)
}

async fn delete_variable(
    authed: ApiAuthed,
    Extension(user_db): Extension<UserDB>,
    Extension(webhook): Extension<WebhookShared>,
    Path((w_id, path)): Path<(String, StripPath)>,
) -> Result<String> {
    let path = path.to_path();
    let mut tx = user_db.begin(&authed).await?;

    sqlx::query!(
        "DELETE FROM variable WHERE path = $1 AND workspace_id = $2",
        path,
        w_id
    )
    .execute(&mut *tx)
    .await?;
    sqlx::query!(
        "DELETE FROM resource WHERE path = $1 AND workspace_id = $2",
        path,
        w_id
    )
    .execute(&mut *tx)
    .await?;
    audit_log(
        &mut *tx,
        &authed.username,
        "variables.delete",
        ActionKind::Delete,
        &w_id,
        Some(path),
        None,
    )
    .await?;

    tx.commit().await?;

    webhook.send_message(
        w_id.clone(),
        WebhookMessage::DeleteVariable { workspace: w_id, path: path.to_owned() },
    );

    Ok(format!("variable {} deleted", path))
}

#[derive(Deserialize)]
struct EditVariable {
    path: Option<String>,
    value: Option<String>,
    is_secret: Option<bool>,
    description: Option<String>,
}

#[derive(Deserialize)]
struct AlreadyEncrypted {
    already_encrypted: Option<bool>,
}

async fn update_variable(
    authed: ApiAuthed,
    Extension(user_db): Extension<UserDB>,
    Extension(webhook): Extension<WebhookShared>,
    Extension(db): Extension<DB>,
    Path((w_id, path)): Path<(String, StripPath)>,
    Query(AlreadyEncrypted { already_encrypted }): Query<AlreadyEncrypted>,
    Json(ns): Json<EditVariable>,
) -> Result<String> {
    use sql_builder::prelude::*;

    let path = path.to_path();
    let authed = maybe_refresh_folders(&path, &w_id, authed, &db).await;

    let mut tx = user_db.begin(&authed).await?;

    let mut sqlb = SqlBuilder::update_table("variable");
    sqlb.and_where_eq("path", "?".bind(&path));
    sqlb.and_where_eq("workspace_id", "?".bind(&w_id));

    if let Some(npath) = &ns.path {
        sqlb.set_str("path", npath);
    }
    let ns_value_is_none = ns.value.is_none();
    if let Some(nvalue) = ns.value {
        let is_secret = if ns.is_secret.is_some() {
            ns.is_secret.unwrap()
        } else {
            sqlx::query_scalar!(
                "SELECT is_secret from variable WHERE path = $1 AND workspace_id = $2",
                &path,
                &w_id
            )
            .fetch_optional(&mut *tx)
            .await?
            .unwrap_or(false)
        };

        let value = if is_secret && !already_encrypted.unwrap_or(false) {
            let mc = build_crypt(&mut tx, &w_id).await?;
            encrypt(&mc, &nvalue)
        } else {
            nvalue
        };
        sqlb.set_str("value", &value);
    }

    if let Some(desc) = ns.description {
        sqlb.set_str("description", &desc);
    }

    if let Some(nbool) = ns.is_secret {
        let old_secret = sqlx::query_scalar!(
            "SELECT is_secret from variable WHERE path = $1 AND workspace_id = $2",
            &path,
            &w_id
        )
        .fetch_optional(&mut *tx)
        .await?
        .unwrap_or(false);
        if old_secret != nbool && ns_value_is_none {
            return Err(Error::BadRequest(
                "cannot change is_secret without updating value too".to_string(),
            ));
        }
        sqlb.set_str("is_secret", nbool);
    }
    sqlb.returning("path");

    if let Some(npath) = ns.path {
        if npath != path {
            check_path_conflict(&mut tx, &w_id, &npath).await?;
            require_owner_of_path(&authed, path)?;

            let mut v = sqlx::query_scalar!(
                "SELECT value FROM resource  WHERE path = $1 AND workspace_id = $2",
                path,
                w_id
            )
            .fetch_optional(&mut *tx)
            .await?
            .flatten();

            if let Some(old_v) = v {
                v = Some(replace_path(
                    old_v,
                    &format!("$var:{path}"),
                    &format!("$var:{npath}"),
                ))
            }

            sqlx::query!(
                "UPDATE resource SET path = $1, value = $2 WHERE path = $3 AND workspace_id = $4",
                npath,
                v,
                path,
                w_id
            )
            .execute(&mut *tx)
            .await?;
        }
    }

    let sql = sqlb.sql().map_err(|e| Error::InternalErr(e.to_string()))?;

    let npath_o: Option<String> = sqlx::query_scalar(&sql).fetch_optional(&mut *tx).await?;

    let npath = not_found_if_none(npath_o, "Variable", path)?;

    audit_log(
        &mut *tx,
        &authed.username,
        "variables.update",
        ActionKind::Update,
        &w_id,
        Some(path),
        None,
    )
    .await?;
    tx.commit().await?;

    webhook.send_message(
        w_id.clone(),
        WebhookMessage::UpdateVariable {
            workspace: w_id,
            old_path: path.to_owned(),
            new_path: npath.clone(),
        },
    );

    Ok(format!("variable {} updated (npath: {:?})", path, npath))
}

fn replace_path(v: serde_json::Value, path: &str, npath: &str) -> Value {
    match v {
        Value::Object(v) => Value::Object(
            v.into_iter()
                .map(|(k, v)| (k, replace_path(v, path, npath)))
                .collect(),
        ),
        Value::Array(arr) => Value::Array(
            arr.into_iter()
                .map(|v| replace_path(v, path, npath))
                .collect(),
        ),
        Value::String(s) if s == path => Value::String(npath.to_owned()),
        _ => v,
    }
}

pub async fn build_crypt<'c>(
    db: &mut Transaction<'c, Postgres>,
    w_id: &str,
) -> Result<MagicCrypt256> {
    let key = get_workspace_key(w_id, db).await?;
    let crypt_key = if let Some(ref salt) = SECRET_SALT.as_ref() {
        format!("{}{}", key, salt)
    } else {
        key
    };
    Ok(magic_crypt::new_magic_crypt!(crypt_key, 256))
}

pub async fn get_workspace_key<'c>(
    w_id: &str,
    db: &mut Transaction<'c, Postgres>,
) -> Result<String> {
    let key = sqlx::query_scalar!(
        "SELECT key FROM workspace_key WHERE workspace_id = $1 AND kind = 'cloud'",
        w_id
    )
    .fetch_one(&mut **db)
    .await
    .map_err(|e| Error::InternalErr(format!("fetching workspace key: {e}")))?;
    Ok(key)
}

pub fn encrypt(mc: &MagicCrypt256, value: &str) -> String {
    mc.encrypt_str_to_base64(value)
}
