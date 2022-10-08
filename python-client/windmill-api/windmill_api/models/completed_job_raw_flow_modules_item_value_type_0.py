from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.completed_job_raw_flow_modules_item_value_type_0_language import (
    CompletedJobRawFlowModulesItemValueType0Language,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CompletedJobRawFlowModulesItemValueType0")


@attr.s(auto_attribs=True)
class CompletedJobRawFlowModulesItemValueType0:
    """
    Attributes:
        content (str):
        language (CompletedJobRawFlowModulesItemValueType0Language):
        type (str):
        path (Union[Unset, str]):
    """

    content: str
    language: CompletedJobRawFlowModulesItemValueType0Language
    type: str
    path: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        content = self.content
        language = self.language.value

        type = self.type
        path = self.path

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
                "language": language,
                "type": type,
            }
        )
        if path is not UNSET:
            field_dict["path"] = path

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        content = d.pop("content")

        language = CompletedJobRawFlowModulesItemValueType0Language(d.pop("language"))

        type = d.pop("type")

        path = d.pop("path", UNSET)

        completed_job_raw_flow_modules_item_value_type_0 = cls(
            content=content,
            language=language,
            type=type,
            path=path,
        )

        completed_job_raw_flow_modules_item_value_type_0.additional_properties = d
        return completed_job_raw_flow_modules_item_value_type_0

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
