from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.metric_type import MetricType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.formula_upset import FormulaUpset


T = TypeVar("T", bound="MetricUpset")


@_attrs_define
class MetricUpset:
    """
    Attributes:
        name (str):
        datasource (str):
        type (MetricType):
        description (Union[Unset, str]):
        unit (Union[Unset, str]):
        source (Union[Unset, str]):
        storage_rule_id (Union[Unset, str]):
        access_zones (Union[List[str], None, Unset]):
        formula (Union[Unset, FormulaUpset]):
    """

    name: str
    datasource: str
    type: MetricType
    description: Union[Unset, str] = UNSET
    unit: Union[Unset, str] = UNSET
    source: Union[Unset, str] = UNSET
    storage_rule_id: Union[Unset, str] = UNSET
    access_zones: Union[List[str], None, Unset] = UNSET
    formula: Union[Unset, "FormulaUpset"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        datasource = self.datasource

        type = self.type.value

        description = self.description

        unit = self.unit

        source = self.source

        storage_rule_id = self.storage_rule_id

        access_zones: Union[List[str], None, Unset]
        if isinstance(self.access_zones, Unset):
            access_zones = UNSET
        elif isinstance(self.access_zones, list):
            access_zones = self.access_zones

        else:
            access_zones = self.access_zones

        formula: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.formula, Unset):
            formula = self.formula.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
                "datasource": datasource,
                "type": type,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if unit is not UNSET:
            field_dict["unit"] = unit
        if source is not UNSET:
            field_dict["source"] = source
        if storage_rule_id is not UNSET:
            field_dict["storageRuleId"] = storage_rule_id
        if access_zones is not UNSET:
            field_dict["accessZones"] = access_zones
        if formula is not UNSET:
            field_dict["formula"] = formula

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.formula_upset import FormulaUpset

        d = src_dict.copy()
        name = d.pop("name")

        datasource = d.pop("datasource")

        type = MetricType(d.pop("type"))

        description = d.pop("description", UNSET)

        unit = d.pop("unit", UNSET)

        source = d.pop("source", UNSET)

        storage_rule_id = d.pop("storageRuleId", UNSET)

        def _parse_access_zones(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                access_zones_type_0 = cast(List[str], data)

                return access_zones_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        access_zones = _parse_access_zones(d.pop("accessZones", UNSET))

        _formula = d.pop("formula", UNSET)
        formula: Union[Unset, FormulaUpset]
        if isinstance(_formula, Unset):
            formula = UNSET
        else:
            formula = FormulaUpset.from_dict(_formula)

        metric_upset = cls(
            name=name,
            datasource=datasource,
            type=type,
            description=description,
            unit=unit,
            source=source,
            storage_rule_id=storage_rule_id,
            access_zones=access_zones,
            formula=formula,
        )

        return metric_upset
