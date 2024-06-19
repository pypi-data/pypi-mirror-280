from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="StorageRuleUpset")


@_attrs_define
class StorageRuleUpset:
    """
    Attributes:
        name (str):
        validity_in_second (Union[Unset, int]):
        precision (Union[Unset, float]):
    """

    name: str
    validity_in_second: Union[Unset, int] = UNSET
    precision: Union[Unset, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        validity_in_second = self.validity_in_second

        precision = self.precision

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
            }
        )
        if validity_in_second is not UNSET:
            field_dict["validityInSecond"] = validity_in_second
        if precision is not UNSET:
            field_dict["precision"] = precision

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        validity_in_second = d.pop("validityInSecond", UNSET)

        precision = d.pop("precision", UNSET)

        storage_rule_upset = cls(
            name=name,
            validity_in_second=validity_in_second,
            precision=precision,
        )

        return storage_rule_upset
