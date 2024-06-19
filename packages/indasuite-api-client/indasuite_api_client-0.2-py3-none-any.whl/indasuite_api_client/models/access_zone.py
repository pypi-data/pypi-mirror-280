from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.access_type import AccessType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AccessZone")


@_attrs_define
class AccessZone:
    """
    Attributes:
        id (Union[Unset, str]):
        name (Union[Unset, str]):
        groups (Union[List[str], None, Unset]):
        access_type (Union[Unset, AccessType]):
        is_default (Union[Unset, bool]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    groups: Union[List[str], None, Unset] = UNSET
    access_type: Union[Unset, AccessType] = UNSET
    is_default: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        groups: Union[List[str], None, Unset]
        if isinstance(self.groups, Unset):
            groups = UNSET
        elif isinstance(self.groups, list):
            groups = self.groups

        else:
            groups = self.groups

        access_type: Union[Unset, str] = UNSET
        if not isinstance(self.access_type, Unset):
            access_type = self.access_type.value

        is_default = self.is_default

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if groups is not UNSET:
            field_dict["groups"] = groups
        if access_type is not UNSET:
            field_dict["accessType"] = access_type
        if is_default is not UNSET:
            field_dict["isDefault"] = is_default

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

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

        _access_type = d.pop("accessType", UNSET)
        access_type: Union[Unset, AccessType]
        if isinstance(_access_type, Unset):
            access_type = UNSET
        else:
            access_type = AccessType(_access_type)

        is_default = d.pop("isDefault", UNSET)

        access_zone = cls(
            id=id,
            name=name,
            groups=groups,
            access_type=access_type,
            is_default=is_default,
        )

        return access_zone
