from enum import Enum

class AuditLogOperation(str, Enum):
    ACCOUNT_DELETE = "account.delete"
    APPS_CREATE = "apps.create"
    APPS_DELETE = "apps.delete"
    APPS_UPDATE = "apps.update"
    FLOWS_ARCHIVE = "flows.archive"
    FLOWS_CREATE = "flows.create"
    FLOWS_DELETE = "flows.delete"
    FLOWS_UPDATE = "flows.update"
    FOLDER_ADD_OWNER = "folder.add_owner"
    FOLDER_CREATE = "folder.create"
    FOLDER_DELETE = "folder.delete"
    FOLDER_REMOVE_OWNER = "folder.remove_owner"
    FOLDER_UPDATE = "folder.update"
    GROUP_ADDUSER = "group.adduser"
    GROUP_CREATE = "group.create"
    GROUP_DELETE = "group.delete"
    GROUP_EDIT = "group.edit"
    GROUP_REMOVEUSER = "group.removeuser"
    IGROUP_ADDUSER = "igroup.adduser"
    IGROUP_CREATE = "igroup.create"
    IGROUP_DELETE = "igroup.delete"
    IGROUP_REMOVEUSER = "igroup.removeuser"
    JOBS = "jobs"
    JOBS_CANCEL = "jobs.cancel"
    JOBS_DELETE = "jobs.delete"
    JOBS_DISAPPROVAL = "jobs.disapproval"
    JOBS_FLOW_DEPENDENCIES = "jobs.flow_dependencies"
    JOBS_FORCE_CANCEL = "jobs.force_cancel"
    JOBS_RUN = "jobs.run"
    JOBS_RUN_DEPENDENCIES = "jobs.run.dependencies"
    JOBS_RUN_FLOW = "jobs.run.flow"
    JOBS_RUN_FLOW_PREVIEW = "jobs.run.flow_preview"
    JOBS_RUN_IDENTITY = "jobs.run.identity"
    JOBS_RUN_NOOP = "jobs.run.noop"
    JOBS_RUN_PREVIEW = "jobs.run.preview"
    JOBS_RUN_SCRIPT = "jobs.run.script"
    JOBS_RUN_SCRIPT_HUB = "jobs.run.script_hub"
    OAUTH_LOGIN = "oauth.login"
    OAUTH_SIGNUP = "oauth.signup"
    OPENAI_REQUEST = "openai.request"
    RESOURCES_CREATE = "resources.create"
    RESOURCES_DELETE = "resources.delete"
    RESOURCES_UPDATE = "resources.update"
    RESOURCE_TYPES_CREATE = "resource_types.create"
    RESOURCE_TYPES_DELETE = "resource_types.delete"
    RESOURCE_TYPES_UPDATE = "resource_types.update"
    SCHEDULE_CREATE = "schedule.create"
    SCHEDULE_DELETE = "schedule.delete"
    SCHEDULE_EDIT = "schedule.edit"
    SCHEDULE_SETENABLED = "schedule.setenabled"
    SCRIPTS_ARCHIVE = "scripts.archive"
    SCRIPTS_CREATE = "scripts.create"
    SCRIPTS_DELETE = "scripts.delete"
    SCRIPTS_UPDATE = "scripts.update"
    USERS_ACCEPT_INVITE = "users.accept_invite"
    USERS_ADD_GLOBAL = "users.add_global"
    USERS_ADD_TO_WORKSPACE = "users.add_to_workspace"
    USERS_CREATE = "users.create"
    USERS_DECLINE_INVITE = "users.decline_invite"
    USERS_DELETE = "users.delete"
    USERS_IMPERSONATE = "users.impersonate"
    USERS_LEAVE_WORKSPACE = "users.leave_workspace"
    USERS_LOGIN = "users.login"
    USERS_LOGOUT = "users.logout"
    USERS_SETPASSWORD = "users.setpassword"
    USERS_TOKEN_CREATE = "users.token.create"
    USERS_TOKEN_DELETE = "users.token.delete"
    USERS_UPDATE = "users.update"
    VARIABLES_CREATE = "variables.create"
    VARIABLES_DECRYPT_SECRET = "variables.decrypt_secret"
    VARIABLES_DELETE = "variables.delete"
    VARIABLES_UPDATE = "variables.update"
    WORKSPACES_ARCHIVE = "workspaces.archive"
    WORKSPACES_CREATE = "workspaces.create"
    WORKSPACES_DELETE = "workspaces.delete"
    WORKSPACES_EDIT_AUTO_INVITE_DOMAIN = "workspaces.edit_auto_invite_domain"
    WORKSPACES_EDIT_COMMAND_SCRIPT = "workspaces.edit_command_script"
    WORKSPACES_EDIT_COPILOT_CONFIG = "workspaces.edit_copilot_config"
    WORKSPACES_EDIT_DEPLOY_TO = "workspaces.edit_deploy_to"
    WORKSPACES_EDIT_ERROR_HANDLER = "workspaces.edit_error_handler"
    WORKSPACES_EDIT_WEBHOOK = "workspaces.edit_webhook"
    WORKSPACES_UNARCHIVE = "workspaces.unarchive"
    WORKSPACES_UPDATE = "workspaces.update"

    def __str__(self) -> str:
        return str(self.value)
