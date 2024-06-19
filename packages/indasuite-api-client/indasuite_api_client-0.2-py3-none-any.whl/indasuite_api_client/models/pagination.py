from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="Pagination")


@_attrs_define
class Pagination:
    """
    Attributes:
        count (Union[Unset, int]):
        is_complete (Union[Unset, bool]):
        pagination_key (Union[Unset, str]):
    """

    count: Union[Unset, int] = UNSET
    is_complete: Union[Unset, bool] = UNSET
    pagination_key: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        count = self.count

        is_complete = self.is_complete

        pagination_key = self.pagination_key

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if is_complete is not UNSET:
            field_dict["isComplete"] = is_complete
        if pagination_key is not UNSET:
            field_dict["paginationKey"] = pagination_key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        count = d.pop("count", UNSET)

        is_complete = d.pop("isComplete", UNSET)

        pagination_key = d.pop("paginationKey", UNSET)

        pagination = cls(
            count=count,
            is_complete=is_complete,
            pagination_key=pagination_key,
        )

        return pagination
