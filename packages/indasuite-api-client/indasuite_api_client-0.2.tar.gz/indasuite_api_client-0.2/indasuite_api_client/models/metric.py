from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.metric_type import MetricType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access_zone import AccessZone
    from ..models.formula import Formula
    from ..models.storage_rule import StorageRule


T = TypeVar("T", bound="Metric")


@_attrs_define
class Metric:
    """
    Attributes:
        description (Union[Unset, str]):
        unit (Union[Unset, str]):
        source (Union[Unset, str]):
        id (Union[Unset, str]):
        name (Union[Unset, str]):
        datasource (Union[Unset, str]):
        type (Union[Unset, MetricType]):
        storage_rule (Union[Unset, StorageRule]):
        access_zones (Union[List['AccessZone'], None, Unset]):
        formula (Union[Unset, Formula]):
    """

    description: Union[Unset, str] = UNSET
    unit: Union[Unset, str] = UNSET
    source: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    datasource: Union[Unset, str] = UNSET
    type: Union[Unset, MetricType] = UNSET
    storage_rule: Union[Unset, "StorageRule"] = UNSET
    access_zones: Union[List["AccessZone"], None, Unset] = UNSET
    formula: Union[Unset, "Formula"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        description = self.description

        unit = self.unit

        source = self.source

        id = self.id

        name = self.name

        datasource = self.datasource

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        storage_rule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.storage_rule, Unset):
            storage_rule = self.storage_rule.to_dict()

        access_zones: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.access_zones, Unset):
            access_zones = UNSET
        elif isinstance(self.access_zones, list):
            access_zones = []
            for access_zones_type_0_item_data in self.access_zones:
                access_zones_type_0_item = access_zones_type_0_item_data.to_dict()
                access_zones.append(access_zones_type_0_item)

        else:
            access_zones = self.access_zones

        formula: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.formula, Unset):
            formula = self.formula.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if unit is not UNSET:
            field_dict["unit"] = unit
        if source is not UNSET:
            field_dict["source"] = source
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if datasource is not UNSET:
            field_dict["datasource"] = datasource
        if type is not UNSET:
            field_dict["type"] = type
        if storage_rule is not UNSET:
            field_dict["storageRule"] = storage_rule
        if access_zones is not UNSET:
            field_dict["accessZones"] = access_zones
        if formula is not UNSET:
            field_dict["formula"] = formula

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.access_zone import AccessZone
        from ..models.formula import Formula
        from ..models.storage_rule import StorageRule

        d = src_dict.copy()
        description = d.pop("description", UNSET)

        unit = d.pop("unit", UNSET)

        source = d.pop("source", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        datasource = d.pop("datasource", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, MetricType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = MetricType(_type)

        _storage_rule = d.pop("storageRule", UNSET)
        storage_rule: Union[Unset, StorageRule]
        if isinstance(_storage_rule, Unset):
            storage_rule = UNSET
        else:
            storage_rule = StorageRule.from_dict(_storage_rule)

        def _parse_access_zones(data: object) -> Union[List["AccessZone"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                access_zones_type_0 = []
                _access_zones_type_0 = data
                for access_zones_type_0_item_data in _access_zones_type_0:
                    access_zones_type_0_item = AccessZone.from_dict(access_zones_type_0_item_data)

                    access_zones_type_0.append(access_zones_type_0_item)

                return access_zones_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["AccessZone"], None, Unset], data)

        access_zones = _parse_access_zones(d.pop("accessZones", UNSET))

        _formula = d.pop("formula", UNSET)
        formula: Union[Unset, Formula]
        if isinstance(_formula, Unset):
            formula = UNSET
        else:
            formula = Formula.from_dict(_formula)

        metric = cls(
            description=description,
            unit=unit,
            source=source,
            id=id,
            name=name,
            datasource=datasource,
            type=type,
            storage_rule=storage_rule,
            access_zones=access_zones,
            formula=formula,
        )

        return metric
