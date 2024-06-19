from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SettingUpdate")


@_attrs_define
class SettingUpdate:
    """
    Attributes:
        future_write_limit_in_minute (Union[Unset, int]):
        enable_partial_write (Union[Unset, bool]):
    """

    future_write_limit_in_minute: Union[Unset, int] = UNSET
    enable_partial_write: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        future_write_limit_in_minute = self.future_write_limit_in_minute

        enable_partial_write = self.enable_partial_write

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if future_write_limit_in_minute is not UNSET:
            field_dict["futureWriteLimitInMinute"] = future_write_limit_in_minute
        if enable_partial_write is not UNSET:
            field_dict["enablePartialWrite"] = enable_partial_write

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        future_write_limit_in_minute = d.pop("futureWriteLimitInMinute", UNSET)

        enable_partial_write = d.pop("enablePartialWrite", UNSET)

        setting_update = cls(
            future_write_limit_in_minute=future_write_limit_in_minute,
            enable_partial_write=enable_partial_write,
        )

        return setting_update
