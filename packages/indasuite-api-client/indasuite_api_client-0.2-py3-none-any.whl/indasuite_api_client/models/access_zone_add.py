from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.access_type import AccessType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AccessZoneAdd")


@_attrs_define
class AccessZoneAdd:
    """
    Attributes:
        name (str):
        access_type (AccessType):
        groups (Union[List[str], None, Unset]):
    """

    name: str
    access_type: AccessType
    groups: Union[List[str], None, Unset] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        access_type = self.access_type.value

        groups: Union[List[str], None, Unset]
        if isinstance(self.groups, Unset):
            groups = UNSET
        elif isinstance(self.groups, list):
            groups = self.groups

        else:
            groups = self.groups

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
                "accessType": access_type,
            }
        )
        if groups is not UNSET:
            field_dict["groups"] = groups

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        access_type = AccessType(d.pop("accessType"))

        def _parse_groups(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                groups_type_0 = cast(List[str], data)

                return groups_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        groups = _parse_groups(d.pop("groups", UNSET))

        access_zone_add = cls(
            name=name,
            access_type=access_type,
            groups=groups,
        )

        return access_zone_add
