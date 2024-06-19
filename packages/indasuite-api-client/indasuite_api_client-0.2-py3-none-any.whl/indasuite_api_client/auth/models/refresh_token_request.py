from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RefreshTokenRequest")


@_attrs_define
class RefreshTokenRequest:
    """
    Attributes:
        refresh_token (str): Refresh token that was retrieved previously
        client_id (str): Unique equipment identifier (format : [DeviceType]-name)
    """

    refresh_token: str
    client_id: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        refresh_token = self.refresh_token

        client_id = self.client_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "refresh_token": refresh_token,
                "client_id": client_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        refresh_token = d.pop("refresh_token")

        client_id = d.pop("client_id")

        refresh_token_request = cls(
            refresh_token=refresh_token,
            client_id=client_id,
        )

        refresh_token_request.additional_properties = d
        return refresh_token_request

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
