from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AnnotationValueUpdate")


@_attrs_define
class AnnotationValueUpdate:
    """
    Attributes:
        old_value (Union[Unset, float]):
        new_value (Union[Unset, float]):
    """

    old_value: Union[Unset, float] = UNSET
    new_value: Union[Unset, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        old_value = self.old_value

        new_value = self.new_value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if old_value is not UNSET:
            field_dict["oldValue"] = old_value
        if new_value is not UNSET:
            field_dict["newValue"] = new_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        old_value = d.pop("oldValue", UNSET)

        new_value = d.pop("newValue", UNSET)

        annotation_value_update = cls(
            old_value=old_value,
            new_value=new_value,
        )

        return annotation_value_update
