from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.template_substitution import TemplateSubstitution
from ..models.template_type import TemplateType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Template")


@attr.s(auto_attribs=True)
class Template:
    """
    Attributes:
        html_part (Union[Unset, str]):
        subject (Union[Unset, str]):
        template_id (Union[Unset, str]):
        sender_id (Union[Unset, str]):
        text_part (Union[Unset, str]):
        type (Union[Unset, TemplateType]):
        substitutions (Union[Unset, List[TemplateSubstitution]]):
        created_at (Union[Unset, str]):
        updated_at (Union[Unset, str]):
    """

    html_part: Union[Unset, str] = UNSET
    subject: Union[Unset, str] = UNSET
    template_id: Union[Unset, str] = UNSET
    sender_id: Union[Unset, str] = UNSET
    text_part: Union[Unset, str] = UNSET
    type: Union[Unset, TemplateType] = UNSET
    substitutions: Union[Unset, List[TemplateSubstitution]] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        html_part = self.html_part
        subject = self.subject
        template_id = self.template_id
        sender_id = self.sender_id
        text_part = self.text_part
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        substitutions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.substitutions, Unset):
            substitutions = []
            for substitutions_item_data in self.substitutions:
                substitutions_item = substitutions_item_data.to_dict()

                substitutions.append(substitutions_item)

        created_at = self.created_at
        updated_at = self.updated_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if html_part is not UNSET:
            field_dict["HtmlPart"] = html_part
        if subject is not UNSET:
            field_dict["Subject"] = subject
        if template_id is not UNSET:
            field_dict["TemplateId"] = template_id
        if sender_id is not UNSET:
            field_dict["SenderId"] = sender_id
        if text_part is not UNSET:
            field_dict["TextPart"] = text_part
        if type is not UNSET:
            field_dict["Type"] = type
        if substitutions is not UNSET:
            field_dict["Substitutions"] = substitutions
        if created_at is not UNSET:
            field_dict["CreatedAt"] = created_at
        if updated_at is not UNSET:
            field_dict["UpdatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        html_part = d.pop("HtmlPart", UNSET)

        subject = d.pop("Subject", UNSET)

        template_id = d.pop("TemplateId", UNSET)

        sender_id = d.pop("SenderId", UNSET)

        text_part = d.pop("TextPart", UNSET)

        _type = d.pop("Type", UNSET)
        type: Union[Unset, TemplateType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = TemplateType(_type)

        substitutions = []
        _substitutions = d.pop("Substitutions", UNSET)
        for substitutions_item_data in _substitutions or []:
            substitutions_item = TemplateSubstitution.from_dict(substitutions_item_data)

            substitutions.append(substitutions_item)

        created_at = d.pop("CreatedAt", UNSET)

        updated_at = d.pop("UpdatedAt", UNSET)

        template = cls(
            html_part=html_part,
            subject=subject,
            template_id=template_id,
            sender_id=sender_id,
            text_part=text_part,
            type=type,
            substitutions=substitutions,
            created_at=created_at,
            updated_at=updated_at,
        )

        template.additional_properties = d
        return template

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
