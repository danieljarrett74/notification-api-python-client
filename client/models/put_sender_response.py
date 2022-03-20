from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.sender import Sender
from ..types import UNSET, Unset

T = TypeVar("T", bound="PutSenderResponse")


@attr.s(auto_attribs=True)
class PutSenderResponse:
    """
    Attributes:
        sender (Union[Unset, Sender]):
    """

    sender: Union[Unset, Sender] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sender: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sender, Unset):
            sender = self.sender.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sender is not UNSET:
            field_dict["sender"] = sender

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _sender = d.pop("sender", UNSET)
        sender: Union[Unset, Sender]
        if isinstance(_sender, Unset):
            sender = UNSET
        else:
            sender = Sender.from_dict(_sender)

        put_sender_response = cls(
            sender=sender,
        )

        put_sender_response.additional_properties = d
        return put_sender_response

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
