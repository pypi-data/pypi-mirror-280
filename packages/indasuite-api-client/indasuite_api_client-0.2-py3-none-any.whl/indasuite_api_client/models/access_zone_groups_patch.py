from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AccessZoneGroupsPatch")


@_attrs_define
class AccessZoneGroupsPatch:
    """
    Attributes:
        groups_to_add (Union[List[str], None, Unset]):
        groups_to_remove (Union[List[str], None, Unset]):
    """

    groups_to_add: Union[List[str], None, Unset] = UNSET
    groups_to_remove: Union[List[str], None, Unset] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        groups_to_add: Union[List[str], None, Unset]
        if isinstance(self.groups_to_add, Unset):
            groups_to_add = UNSET
        elif isinstance(self.groups_to_add, list):
            groups_to_add = self.groups_to_add

        else:
            groups_to_add = self.groups_to_add

        groups_to_remove: Union[List[str], None, Unset]
        if isinstance(self.groups_to_remove, Unset):
            groups_to_remove = UNSET
        elif isinstance(self.groups_to_remove, list):
            groups_to_remove = self.groups_to_remove

        else:
            groups_to_remove = self.groups_to_remove

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if groups_to_add is not UNSET:
            field_dict["groupsToAdd"] = groups_to_add
        if groups_to_remove is not UNSET:
            field_dict["groupsToRemove"] = groups_to_remove

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_groups_to_add(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                groups_to_add_type_0 = cast(List[str], data)

                return groups_to_add_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        groups_to_add = _parse_groups_to_add(d.pop("groupsToAdd", UNSET))

        def _parse_groups_to_remove(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                groups_to_remove_type_0 = cast(List[str], data)

                return groups_to_remove_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        groups_to_remove = _parse_groups_to_remove(d.pop("groupsToRemove", UNSET))

        access_zone_groups_patch = cls(
            groups_to_add=groups_to_add,
            groups_to_remove=groups_to_remove,
        )

        return access_zone_groups_patch
