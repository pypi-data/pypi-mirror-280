from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ...types import UNSET, Unset


T = TypeVar("T", bound="ResponseWithToken")


@_attrs_define
class ResponseWithToken:
    """
    Attributes:

        access_token (Union[Unset, str]):
        scope (Union[Unset, str]):
        expires_in (Union[Unset, int]):
        token_type (Union[Unset, str]):
    """

    access_token: Union[Unset, str] = UNSET
    scope: Union[Unset, str] = UNSET
    expires_in: Union[Unset, int] = UNSET
    token_type: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        access_token = self.access_token
        scope = self.scope
        expires_in = self.expires_in
        token_type = self.token_type

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if access_token is not UNSET:
            field_dict["access_token"] = access_token
        if scope is not UNSET:
            field_dict["scope"] = scope
        if expires_in is not UNSET:
            field_dict["expires_in"] = expires_in
        if token_type is not UNSET:
            field_dict["token_type"] = token_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ...models.access_zone import AccessZone

        d = src_dict.copy()

        access_token = d.pop("access_token", UNSET)
        scope = d.pop("scope", UNSET)
        expires_in = d.pop("expires_in", UNSET)
        token_type = d.pop("token_type", UNSET)

        response_with_access_zone = cls(
            access_token=access_token,
            scope=scope,
            expires_in=expires_in,
            token_type=token_type,
        )

        return response_with_access_zone
