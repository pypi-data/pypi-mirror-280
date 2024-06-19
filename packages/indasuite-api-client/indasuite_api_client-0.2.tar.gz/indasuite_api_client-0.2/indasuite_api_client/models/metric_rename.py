from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="MetricRename")


@_attrs_define
class MetricRename:
    """
    Attributes:
        new_name (str):
    """

    new_name: str

    def to_dict(self) -> Dict[str, Any]:
        new_name = self.new_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "newName": new_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        new_name = d.pop("newName")

        metric_rename = cls(
            new_name=new_name,
        )

        return metric_rename
