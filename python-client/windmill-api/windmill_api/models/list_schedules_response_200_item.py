from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Union
from typing import cast
from typing import Dict
import datetime
from dateutil.parser import isoparse
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.list_schedules_response_200_item_args import ListSchedulesResponse200ItemArgs
  from ..models.list_schedules_response_200_item_retry import ListSchedulesResponse200ItemRetry
  from ..models.list_schedules_response_200_item_extra_perms import ListSchedulesResponse200ItemExtraPerms
  from ..models.list_schedules_response_200_item_on_failure_extra_args import ListSchedulesResponse200ItemOnFailureExtraArgs
  from ..models.list_schedules_response_200_item_on_recovery_extra_args import ListSchedulesResponse200ItemOnRecoveryExtraArgs





T = TypeVar("T", bound="ListSchedulesResponse200Item")


@_attrs_define
class ListSchedulesResponse200Item:
    """ 
        Attributes:
            path (str):
            edited_by (str):
            edited_at (datetime.datetime):
            schedule (str):
            timezone (str):
            enabled (bool):
            script_path (str):
            is_flow (bool):
            extra_perms (ListSchedulesResponse200ItemExtraPerms):
            email (str):
            args (Union[Unset, ListSchedulesResponse200ItemArgs]):
            error (Union[Unset, str]):
            on_failure (Union[Unset, str]):
            on_failure_times (Union[Unset, float]):
            on_failure_exact (Union[Unset, bool]):
            on_failure_extra_args (Union[Unset, ListSchedulesResponse200ItemOnFailureExtraArgs]):
            on_recovery (Union[Unset, str]):
            on_recovery_times (Union[Unset, float]):
            on_recovery_extra_args (Union[Unset, ListSchedulesResponse200ItemOnRecoveryExtraArgs]):
            ws_error_handler_muted (Union[Unset, bool]):
            retry (Union[Unset, ListSchedulesResponse200ItemRetry]):
            summary (Union[Unset, str]):
            no_flow_overlap (Union[Unset, bool]):
            tag (Union[Unset, str]):
     """

    path: str
    edited_by: str
    edited_at: datetime.datetime
    schedule: str
    timezone: str
    enabled: bool
    script_path: str
    is_flow: bool
    extra_perms: 'ListSchedulesResponse200ItemExtraPerms'
    email: str
    args: Union[Unset, 'ListSchedulesResponse200ItemArgs'] = UNSET
    error: Union[Unset, str] = UNSET
    on_failure: Union[Unset, str] = UNSET
    on_failure_times: Union[Unset, float] = UNSET
    on_failure_exact: Union[Unset, bool] = UNSET
    on_failure_extra_args: Union[Unset, 'ListSchedulesResponse200ItemOnFailureExtraArgs'] = UNSET
    on_recovery: Union[Unset, str] = UNSET
    on_recovery_times: Union[Unset, float] = UNSET
    on_recovery_extra_args: Union[Unset, 'ListSchedulesResponse200ItemOnRecoveryExtraArgs'] = UNSET
    ws_error_handler_muted: Union[Unset, bool] = UNSET
    retry: Union[Unset, 'ListSchedulesResponse200ItemRetry'] = UNSET
    summary: Union[Unset, str] = UNSET
    no_flow_overlap: Union[Unset, bool] = UNSET
    tag: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.list_schedules_response_200_item_args import ListSchedulesResponse200ItemArgs
        from ..models.list_schedules_response_200_item_retry import ListSchedulesResponse200ItemRetry
        from ..models.list_schedules_response_200_item_extra_perms import ListSchedulesResponse200ItemExtraPerms
        from ..models.list_schedules_response_200_item_on_failure_extra_args import ListSchedulesResponse200ItemOnFailureExtraArgs
        from ..models.list_schedules_response_200_item_on_recovery_extra_args import ListSchedulesResponse200ItemOnRecoveryExtraArgs
        path = self.path
        edited_by = self.edited_by
        edited_at = self.edited_at.isoformat()

        schedule = self.schedule
        timezone = self.timezone
        enabled = self.enabled
        script_path = self.script_path
        is_flow = self.is_flow
        extra_perms = self.extra_perms.to_dict()

        email = self.email
        args: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.args, Unset):
            args = self.args.to_dict()

        error = self.error
        on_failure = self.on_failure
        on_failure_times = self.on_failure_times
        on_failure_exact = self.on_failure_exact
        on_failure_extra_args: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.on_failure_extra_args, Unset):
            on_failure_extra_args = self.on_failure_extra_args.to_dict()

        on_recovery = self.on_recovery
        on_recovery_times = self.on_recovery_times
        on_recovery_extra_args: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.on_recovery_extra_args, Unset):
            on_recovery_extra_args = self.on_recovery_extra_args.to_dict()

        ws_error_handler_muted = self.ws_error_handler_muted
        retry: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.retry, Unset):
            retry = self.retry.to_dict()

        summary = self.summary
        no_flow_overlap = self.no_flow_overlap
        tag = self.tag

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "path": path,
            "edited_by": edited_by,
            "edited_at": edited_at,
            "schedule": schedule,
            "timezone": timezone,
            "enabled": enabled,
            "script_path": script_path,
            "is_flow": is_flow,
            "extra_perms": extra_perms,
            "email": email,
        })
        if args is not UNSET:
            field_dict["args"] = args
        if error is not UNSET:
            field_dict["error"] = error
        if on_failure is not UNSET:
            field_dict["on_failure"] = on_failure
        if on_failure_times is not UNSET:
            field_dict["on_failure_times"] = on_failure_times
        if on_failure_exact is not UNSET:
            field_dict["on_failure_exact"] = on_failure_exact
        if on_failure_extra_args is not UNSET:
            field_dict["on_failure_extra_args"] = on_failure_extra_args
        if on_recovery is not UNSET:
            field_dict["on_recovery"] = on_recovery
        if on_recovery_times is not UNSET:
            field_dict["on_recovery_times"] = on_recovery_times
        if on_recovery_extra_args is not UNSET:
            field_dict["on_recovery_extra_args"] = on_recovery_extra_args
        if ws_error_handler_muted is not UNSET:
            field_dict["ws_error_handler_muted"] = ws_error_handler_muted
        if retry is not UNSET:
            field_dict["retry"] = retry
        if summary is not UNSET:
            field_dict["summary"] = summary
        if no_flow_overlap is not UNSET:
            field_dict["no_flow_overlap"] = no_flow_overlap
        if tag is not UNSET:
            field_dict["tag"] = tag

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.list_schedules_response_200_item_args import ListSchedulesResponse200ItemArgs
        from ..models.list_schedules_response_200_item_retry import ListSchedulesResponse200ItemRetry
        from ..models.list_schedules_response_200_item_extra_perms import ListSchedulesResponse200ItemExtraPerms
        from ..models.list_schedules_response_200_item_on_failure_extra_args import ListSchedulesResponse200ItemOnFailureExtraArgs
        from ..models.list_schedules_response_200_item_on_recovery_extra_args import ListSchedulesResponse200ItemOnRecoveryExtraArgs
        d = src_dict.copy()
        path = d.pop("path")

        edited_by = d.pop("edited_by")

        edited_at = isoparse(d.pop("edited_at"))




        schedule = d.pop("schedule")

        timezone = d.pop("timezone")

        enabled = d.pop("enabled")

        script_path = d.pop("script_path")

        is_flow = d.pop("is_flow")

        extra_perms = ListSchedulesResponse200ItemExtraPerms.from_dict(d.pop("extra_perms"))




        email = d.pop("email")

        _args = d.pop("args", UNSET)
        args: Union[Unset, ListSchedulesResponse200ItemArgs]
        if isinstance(_args,  Unset):
            args = UNSET
        else:
            args = ListSchedulesResponse200ItemArgs.from_dict(_args)




        error = d.pop("error", UNSET)

        on_failure = d.pop("on_failure", UNSET)

        on_failure_times = d.pop("on_failure_times", UNSET)

        on_failure_exact = d.pop("on_failure_exact", UNSET)

        _on_failure_extra_args = d.pop("on_failure_extra_args", UNSET)
        on_failure_extra_args: Union[Unset, ListSchedulesResponse200ItemOnFailureExtraArgs]
        if isinstance(_on_failure_extra_args,  Unset):
            on_failure_extra_args = UNSET
        else:
            on_failure_extra_args = ListSchedulesResponse200ItemOnFailureExtraArgs.from_dict(_on_failure_extra_args)




        on_recovery = d.pop("on_recovery", UNSET)

        on_recovery_times = d.pop("on_recovery_times", UNSET)

        _on_recovery_extra_args = d.pop("on_recovery_extra_args", UNSET)
        on_recovery_extra_args: Union[Unset, ListSchedulesResponse200ItemOnRecoveryExtraArgs]
        if isinstance(_on_recovery_extra_args,  Unset):
            on_recovery_extra_args = UNSET
        else:
            on_recovery_extra_args = ListSchedulesResponse200ItemOnRecoveryExtraArgs.from_dict(_on_recovery_extra_args)




        ws_error_handler_muted = d.pop("ws_error_handler_muted", UNSET)

        _retry = d.pop("retry", UNSET)
        retry: Union[Unset, ListSchedulesResponse200ItemRetry]
        if isinstance(_retry,  Unset):
            retry = UNSET
        else:
            retry = ListSchedulesResponse200ItemRetry.from_dict(_retry)




        summary = d.pop("summary", UNSET)

        no_flow_overlap = d.pop("no_flow_overlap", UNSET)

        tag = d.pop("tag", UNSET)

        list_schedules_response_200_item = cls(
            path=path,
            edited_by=edited_by,
            edited_at=edited_at,
            schedule=schedule,
            timezone=timezone,
            enabled=enabled,
            script_path=script_path,
            is_flow=is_flow,
            extra_perms=extra_perms,
            email=email,
            args=args,
            error=error,
            on_failure=on_failure,
            on_failure_times=on_failure_times,
            on_failure_exact=on_failure_exact,
            on_failure_extra_args=on_failure_extra_args,
            on_recovery=on_recovery,
            on_recovery_times=on_recovery_times,
            on_recovery_extra_args=on_recovery_extra_args,
            ws_error_handler_muted=ws_error_handler_muted,
            retry=retry,
            summary=summary,
            no_flow_overlap=no_flow_overlap,
            tag=tag,
        )

        list_schedules_response_200_item.additional_properties = d
        return list_schedules_response_200_item

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
