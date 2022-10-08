from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.flow_value_failure_module_input_transforms_additional_property_type_0 import (
    FlowValueFailureModuleInputTransformsAdditionalPropertyType0,
)
from ..models.flow_value_failure_module_input_transforms_additional_property_type_1 import (
    FlowValueFailureModuleInputTransformsAdditionalPropertyType1,
)

T = TypeVar("T", bound="FlowValueFailureModuleInputTransforms")


@attr.s(auto_attribs=True)
class FlowValueFailureModuleInputTransforms:
    """ """

    additional_properties: Dict[
        str,
        Union[
            FlowValueFailureModuleInputTransformsAdditionalPropertyType0,
            FlowValueFailureModuleInputTransformsAdditionalPropertyType1,
        ],
    ] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():

            if isinstance(prop, FlowValueFailureModuleInputTransformsAdditionalPropertyType0):
                field_dict[prop_name] = prop.to_dict()

            else:
                field_dict[prop_name] = prop.to_dict()

        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        flow_value_failure_module_input_transforms = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():

            def _parse_additional_property(
                data: object,
            ) -> Union[
                FlowValueFailureModuleInputTransformsAdditionalPropertyType0,
                FlowValueFailureModuleInputTransformsAdditionalPropertyType1,
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_0 = FlowValueFailureModuleInputTransformsAdditionalPropertyType0.from_dict(
                        data
                    )

                    return additional_property_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                additional_property_type_1 = FlowValueFailureModuleInputTransformsAdditionalPropertyType1.from_dict(
                    data
                )

                return additional_property_type_1

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        flow_value_failure_module_input_transforms.additional_properties = additional_properties
        return flow_value_failure_module_input_transforms

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(
        self, key: str
    ) -> Union[
        FlowValueFailureModuleInputTransformsAdditionalPropertyType0,
        FlowValueFailureModuleInputTransformsAdditionalPropertyType1,
    ]:
        return self.additional_properties[key]

    def __setitem__(
        self,
        key: str,
        value: Union[
            FlowValueFailureModuleInputTransformsAdditionalPropertyType0,
            FlowValueFailureModuleInputTransformsAdditionalPropertyType1,
        ],
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
