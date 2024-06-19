from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="StorageRule")


@_attrs_define
class StorageRule:
    """
    Attributes:
        id (Union[Unset, str]):
        name (Union[Unset, str]):
        precision (Union[Unset, float]):
        validity_in_second (Union[Unset, int]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    precision: Union[Unset, float] = UNSET
    validity_in_second: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        precision = self.precision

        validity_in_second = self.validity_in_second

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if precision is not UNSET:
            field_dict["precision"] = precision
        if validity_in_second is not UNSET:
            field_dict["validityInSecond"] = validity_in_second

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        precision = d.pop("precision", UNSET)

        validity_in_second = d.pop("validityInSecond", UNSET)

        storage_rule = cls(
            id=id,
            name=name,
            precision=precision,
            validity_in_second=validity_in_second,
        )

        return storage_rule
