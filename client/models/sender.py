from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Sender")


@attr.s(auto_attribs=True)
class Sender:
    """
    Attributes:
        sender_id (str):
        email_address (str):
        name (Union[Unset, str]):
        user_pool_id (Union[Unset, str]):
        created_at (Union[Unset, str]):
        updated_at (Union[Unset, str]):
    """

    sender_id: str
    email_address: str
    name: Union[Unset, str] = UNSET
    user_pool_id: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sender_id = self.sender_id
        email_address = self.email_address
        name = self.name
        user_pool_id = self.user_pool_id
        created_at = self.created_at
        updated_at = self.updated_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "SenderId": sender_id,
                "EmailAddress": email_address,
            }
        )
        if name is not UNSET:
            field_dict["Name"] = name
        if user_pool_id is not UNSET:
            field_dict["UserPoolId"] = user_pool_id
        if created_at is not UNSET:
            field_dict["CreatedAt"] = created_at
        if updated_at is not UNSET:
            field_dict["UpdatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        sender_id = d.pop("SenderId")

        email_address = d.pop("EmailAddress")

        name = d.pop("Name", UNSET)

        user_pool_id = d.pop("UserPoolId", UNSET)

        created_at = d.pop("CreatedAt", UNSET)

        updated_at = d.pop("UpdatedAt", UNSET)

        sender = cls(
            sender_id=sender_id,
            email_address=email_address,
            name=name,
            user_pool_id=user_pool_id,
            created_at=created_at,
            updated_at=updated_at,
        )

        sender.additional_properties = d
        return sender

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
