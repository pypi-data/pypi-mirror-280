from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="Error")


@_attrs_define
class Error:
    """
    Attributes:
        error (Union[Unset, str]):
        message (Union[Unset, str]):
    """

    error: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        error = self.error

        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if error is not UNSET:
            field_dict["error"] = error
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        error = d.pop("error", UNSET)

        message = d.pop("message", UNSET)

        error = cls(
            error=error,
            message=message,
        )

        return error
