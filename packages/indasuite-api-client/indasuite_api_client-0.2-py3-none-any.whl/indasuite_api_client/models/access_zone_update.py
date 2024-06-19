from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

from ..models.access_type import AccessType

T = TypeVar("T", bound="AccessZoneUpdate")


@_attrs_define
class AccessZoneUpdate:
    """
    Attributes:
        name (str):
        access_type (AccessType):
    """

    name: str
    access_type: AccessType

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        access_type = self.access_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
                "accessType": access_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        access_type = AccessType(d.pop("accessType"))

        access_zone_update = cls(
            name=name,
            access_type=access_type,
        )

        return access_zone_update
