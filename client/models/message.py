from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.substitution import Substitution
from ..types import UNSET, Unset

T = TypeVar("T", bound="Message")


@attr.s(auto_attribs=True)
class Message:
    """
    Attributes:
        template_id (str):
        recipient_email (str):
        sender_id (Union[Unset, str]):
        substitutions (Union[Unset, List[Substitution]]):
    """

    template_id: str
    recipient_email: str
    sender_id: Union[Unset, str] = UNSET
    substitutions: Union[Unset, List[Substitution]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        template_id = self.template_id
        recipient_email = self.recipient_email
        sender_id = self.sender_id
        substitutions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.substitutions, Unset):
            substitutions = []
            for substitutions_item_data in self.substitutions:
                substitutions_item = substitutions_item_data.to_dict()

                substitutions.append(substitutions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "TemplateId": template_id,
                "RecipientEmail": recipient_email,
            }
        )
        if sender_id is not UNSET:
            field_dict["SenderId"] = sender_id
        if substitutions is not UNSET:
            field_dict["Substitutions"] = substitutions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        template_id = d.pop("TemplateId")

        recipient_email = d.pop("RecipientEmail")

        sender_id = d.pop("SenderId", UNSET)

        substitutions = []
        _substitutions = d.pop("Substitutions", UNSET)
        for substitutions_item_data in _substitutions or []:
            substitutions_item = Substitution.from_dict(substitutions_item_data)

            substitutions.append(substitutions_item)

        message = cls(
            template_id=template_id,
            recipient_email=recipient_email,
            sender_id=sender_id,
            substitutions=substitutions,
        )

        message.additional_properties = d
        return message

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
