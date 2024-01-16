from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Union
from typing import cast
from typing import cast, List
from typing import Dict
from ..models.get_script_by_path_with_draft_response_200_kind import GetScriptByPathWithDraftResponse200Kind
from ..models.get_script_by_path_with_draft_response_200_language import GetScriptByPathWithDraftResponse200Language
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.get_script_by_path_with_draft_response_200_draft import GetScriptByPathWithDraftResponse200Draft
  from ..models.get_script_by_path_with_draft_response_200_schema import GetScriptByPathWithDraftResponse200Schema





T = TypeVar("T", bound="GetScriptByPathWithDraftResponse200")


@_attrs_define
class GetScriptByPathWithDraftResponse200:
    """ 
        Attributes:
            path (str):
            summary (str):
            description (str):
            content (str):
            language (GetScriptByPathWithDraftResponse200Language):
            hash_ (str):
            parent_hash (Union[Unset, str]):
            schema (Union[Unset, GetScriptByPathWithDraftResponse200Schema]):
            is_template (Union[Unset, bool]):
            lock (Union[Unset, List[str]]):
            kind (Union[Unset, GetScriptByPathWithDraftResponse200Kind]):
            tag (Union[Unset, str]):
            draft_only (Union[Unset, bool]):
            envs (Union[Unset, List[str]]):
            concurrent_limit (Union[Unset, int]):
            concurrency_time_window_s (Union[Unset, int]):
            cache_ttl (Union[Unset, float]):
            dedicated_worker (Union[Unset, bool]):
            ws_error_handler_muted (Union[Unset, bool]):
            priority (Union[Unset, int]):
            restart_unless_cancelled (Union[Unset, bool]):
            timeout (Union[Unset, int]):
            delete_after_use (Union[Unset, bool]):
            deployment_message (Union[Unset, str]):
            draft (Union[Unset, GetScriptByPathWithDraftResponse200Draft]):
     """

    path: str
    summary: str
    description: str
    content: str
    language: GetScriptByPathWithDraftResponse200Language
    hash_: str
    parent_hash: Union[Unset, str] = UNSET
    schema: Union[Unset, 'GetScriptByPathWithDraftResponse200Schema'] = UNSET
    is_template: Union[Unset, bool] = UNSET
    lock: Union[Unset, List[str]] = UNSET
    kind: Union[Unset, GetScriptByPathWithDraftResponse200Kind] = UNSET
    tag: Union[Unset, str] = UNSET
    draft_only: Union[Unset, bool] = UNSET
    envs: Union[Unset, List[str]] = UNSET
    concurrent_limit: Union[Unset, int] = UNSET
    concurrency_time_window_s: Union[Unset, int] = UNSET
    cache_ttl: Union[Unset, float] = UNSET
    dedicated_worker: Union[Unset, bool] = UNSET
    ws_error_handler_muted: Union[Unset, bool] = UNSET
    priority: Union[Unset, int] = UNSET
    restart_unless_cancelled: Union[Unset, bool] = UNSET
    timeout: Union[Unset, int] = UNSET
    delete_after_use: Union[Unset, bool] = UNSET
    deployment_message: Union[Unset, str] = UNSET
    draft: Union[Unset, 'GetScriptByPathWithDraftResponse200Draft'] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.get_script_by_path_with_draft_response_200_draft import GetScriptByPathWithDraftResponse200Draft
        from ..models.get_script_by_path_with_draft_response_200_schema import GetScriptByPathWithDraftResponse200Schema
        path = self.path
        summary = self.summary
        description = self.description
        content = self.content
        language = self.language.value

        hash_ = self.hash_
        parent_hash = self.parent_hash
        schema: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.schema, Unset):
            schema = self.schema.to_dict()

        is_template = self.is_template
        lock: Union[Unset, List[str]] = UNSET
        if not isinstance(self.lock, Unset):
            lock = self.lock




        kind: Union[Unset, str] = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        tag = self.tag
        draft_only = self.draft_only
        envs: Union[Unset, List[str]] = UNSET
        if not isinstance(self.envs, Unset):
            envs = self.envs




        concurrent_limit = self.concurrent_limit
        concurrency_time_window_s = self.concurrency_time_window_s
        cache_ttl = self.cache_ttl
        dedicated_worker = self.dedicated_worker
        ws_error_handler_muted = self.ws_error_handler_muted
        priority = self.priority
        restart_unless_cancelled = self.restart_unless_cancelled
        timeout = self.timeout
        delete_after_use = self.delete_after_use
        deployment_message = self.deployment_message
        draft: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.draft, Unset):
            draft = self.draft.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "path": path,
            "summary": summary,
            "description": description,
            "content": content,
            "language": language,
            "hash": hash_,
        })
        if parent_hash is not UNSET:
            field_dict["parent_hash"] = parent_hash
        if schema is not UNSET:
            field_dict["schema"] = schema
        if is_template is not UNSET:
            field_dict["is_template"] = is_template
        if lock is not UNSET:
            field_dict["lock"] = lock
        if kind is not UNSET:
            field_dict["kind"] = kind
        if tag is not UNSET:
            field_dict["tag"] = tag
        if draft_only is not UNSET:
            field_dict["draft_only"] = draft_only
        if envs is not UNSET:
            field_dict["envs"] = envs
        if concurrent_limit is not UNSET:
            field_dict["concurrent_limit"] = concurrent_limit
        if concurrency_time_window_s is not UNSET:
            field_dict["concurrency_time_window_s"] = concurrency_time_window_s
        if cache_ttl is not UNSET:
            field_dict["cache_ttl"] = cache_ttl
        if dedicated_worker is not UNSET:
            field_dict["dedicated_worker"] = dedicated_worker
        if ws_error_handler_muted is not UNSET:
            field_dict["ws_error_handler_muted"] = ws_error_handler_muted
        if priority is not UNSET:
            field_dict["priority"] = priority
        if restart_unless_cancelled is not UNSET:
            field_dict["restart_unless_cancelled"] = restart_unless_cancelled
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if delete_after_use is not UNSET:
            field_dict["delete_after_use"] = delete_after_use
        if deployment_message is not UNSET:
            field_dict["deployment_message"] = deployment_message
        if draft is not UNSET:
            field_dict["draft"] = draft

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_script_by_path_with_draft_response_200_draft import GetScriptByPathWithDraftResponse200Draft
        from ..models.get_script_by_path_with_draft_response_200_schema import GetScriptByPathWithDraftResponse200Schema
        d = src_dict.copy()
        path = d.pop("path")

        summary = d.pop("summary")

        description = d.pop("description")

        content = d.pop("content")

        language = GetScriptByPathWithDraftResponse200Language(d.pop("language"))




        hash_ = d.pop("hash")

        parent_hash = d.pop("parent_hash", UNSET)

        _schema = d.pop("schema", UNSET)
        schema: Union[Unset, GetScriptByPathWithDraftResponse200Schema]
        if isinstance(_schema,  Unset):
            schema = UNSET
        else:
            schema = GetScriptByPathWithDraftResponse200Schema.from_dict(_schema)




        is_template = d.pop("is_template", UNSET)

        lock = cast(List[str], d.pop("lock", UNSET))


        _kind = d.pop("kind", UNSET)
        kind: Union[Unset, GetScriptByPathWithDraftResponse200Kind]
        if isinstance(_kind,  Unset):
            kind = UNSET
        else:
            kind = GetScriptByPathWithDraftResponse200Kind(_kind)




        tag = d.pop("tag", UNSET)

        draft_only = d.pop("draft_only", UNSET)

        envs = cast(List[str], d.pop("envs", UNSET))


        concurrent_limit = d.pop("concurrent_limit", UNSET)

        concurrency_time_window_s = d.pop("concurrency_time_window_s", UNSET)

        cache_ttl = d.pop("cache_ttl", UNSET)

        dedicated_worker = d.pop("dedicated_worker", UNSET)

        ws_error_handler_muted = d.pop("ws_error_handler_muted", UNSET)

        priority = d.pop("priority", UNSET)

        restart_unless_cancelled = d.pop("restart_unless_cancelled", UNSET)

        timeout = d.pop("timeout", UNSET)

        delete_after_use = d.pop("delete_after_use", UNSET)

        deployment_message = d.pop("deployment_message", UNSET)

        _draft = d.pop("draft", UNSET)
        draft: Union[Unset, GetScriptByPathWithDraftResponse200Draft]
        if isinstance(_draft,  Unset):
            draft = UNSET
        else:
            draft = GetScriptByPathWithDraftResponse200Draft.from_dict(_draft)




        get_script_by_path_with_draft_response_200 = cls(
            path=path,
            summary=summary,
            description=description,
            content=content,
            language=language,
            hash_=hash_,
            parent_hash=parent_hash,
            schema=schema,
            is_template=is_template,
            lock=lock,
            kind=kind,
            tag=tag,
            draft_only=draft_only,
            envs=envs,
            concurrent_limit=concurrent_limit,
            concurrency_time_window_s=concurrency_time_window_s,
            cache_ttl=cache_ttl,
            dedicated_worker=dedicated_worker,
            ws_error_handler_muted=ws_error_handler_muted,
            priority=priority,
            restart_unless_cancelled=restart_unless_cancelled,
            timeout=timeout,
            delete_after_use=delete_after_use,
            deployment_message=deployment_message,
            draft=draft,
        )

        get_script_by_path_with_draft_response_200.additional_properties = d
        return get_script_by_path_with_draft_response_200

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
