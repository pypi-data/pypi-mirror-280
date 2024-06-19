from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.formula_result_type import FormulaResultType
from ..types import UNSET, Unset

T = TypeVar("T", bound="FormulaUpset")


@_attrs_define
class FormulaUpset:
    """
    Attributes:
        formula (str):
        schedule (Union[Unset, str]):
        source_validity_in_second (Union[Unset, int]):
        result_type (Union[Unset, FormulaResultType]):
        timezone (Union[Unset, str]): Type format Iana timezone
        enabled (Union[Unset, bool]):
    """

    formula: str
    schedule: Union[Unset, str] = UNSET
    source_validity_in_second: Union[Unset, int] = UNSET
    result_type: Union[Unset, FormulaResultType] = UNSET
    timezone: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        formula = self.formula

        schedule = self.schedule

        source_validity_in_second = self.source_validity_in_second

        result_type: Union[Unset, str] = UNSET
        if not isinstance(self.result_type, Unset):
            result_type = self.result_type.value

        timezone = self.timezone

        enabled = self.enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "formula": formula,
            }
        )
        if schedule is not UNSET:
            field_dict["schedule"] = schedule
        if source_validity_in_second is not UNSET:
            field_dict["sourceValidityInSecond"] = source_validity_in_second
        if result_type is not UNSET:
            field_dict["resultType"] = result_type
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        formula = d.pop("formula")

        schedule = d.pop("schedule", UNSET)

        source_validity_in_second = d.pop("sourceValidityInSecond", UNSET)

        _result_type = d.pop("resultType", UNSET)
        result_type: Union[Unset, FormulaResultType]
        if isinstance(_result_type, Unset):
            result_type = UNSET
        else:
            result_type = FormulaResultType(_result_type)

        timezone = d.pop("timezone", UNSET)

        enabled = d.pop("enabled", UNSET)

        formula_upset = cls(
            formula=formula,
            schedule=schedule,
            source_validity_in_second=source_validity_in_second,
            result_type=result_type,
            timezone=timezone,
            enabled=enabled,
        )

        return formula_upset
