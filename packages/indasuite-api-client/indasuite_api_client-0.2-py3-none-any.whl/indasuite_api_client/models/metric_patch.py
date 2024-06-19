from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="MetricPatch")


@_attrs_define
class MetricPatch:
    """
    Attributes:
        access_zones_id (Union[List[str], None, Unset]):
        storage_rule_id (Union[Unset, str]):
    """

    access_zones_id: Union[List[str], None, Unset] = UNSET
    storage_rule_id: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        access_zones_id: Union[List[str], None, Unset]
        if isinstance(self.access_zones_id, Unset):
            access_zones_id = UNSET
        elif isinstance(self.access_zones_id, list):
            access_zones_id = self.access_zones_id

        else:
            access_zones_id = self.access_zones_id

        storage_rule_id = self.storage_rule_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if access_zones_id is not UNSET:
            field_dict["accessZonesId"] = access_zones_id
        if storage_rule_id is not UNSET:
            field_dict["storageRuleId"] = storage_rule_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_access_zones_id(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                access_zones_id_type_0 = cast(List[str], data)

                return access_zones_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        access_zones_id = _parse_access_zones_id(d.pop("accessZonesId", UNSET))

        storage_rule_id = d.pop("storageRuleId", UNSET)

        metric_patch = cls(
            access_zones_id=access_zones_id,
            storage_rule_id=storage_rule_id,
        )

        return metric_patch
