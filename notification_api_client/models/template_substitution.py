from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="TemplateSubstitution")


@attr.s(auto_attribs=True)
class TemplateSubstitution:
    """
    Attributes:
        name (Union[Unset, str]):
        default_value (Union[Unset, str]):
        required (Union[Unset, bool]):
    """

    name: Union[Unset, str] = UNSET
    default_value: Union[Unset, str] = UNSET
    required: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        default_value = self.default_value
        required = self.required

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if default_value is not UNSET:
            field_dict["DefaultValue"] = default_value
        if required is not UNSET:
            field_dict["Required"] = required

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("Name", UNSET)

        default_value = d.pop("DefaultValue", UNSET)

        required = d.pop("Required", UNSET)

        template_substitution = cls(
            name=name,
            default_value=default_value,
            required=required,
        )

        template_substitution.additional_properties = d
        return template_substitution

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
