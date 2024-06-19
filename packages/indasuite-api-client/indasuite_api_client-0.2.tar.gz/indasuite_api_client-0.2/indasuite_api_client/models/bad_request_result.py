from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="BadRequestResult")


@_attrs_define
class BadRequestResult:
    """
    Attributes:
        status_code (Union[Unset, int]):
    """

    status_code: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        status_code = self.status_code

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if status_code is not UNSET:
            field_dict["statusCode"] = status_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        status_code = d.pop("statusCode", UNSET)

        bad_request_result = cls(
            status_code=status_code,
        )

        return bad_request_result
