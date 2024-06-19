from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metric_name import MetricName


T = TypeVar("T", bound="Latest")


@_attrs_define
class Latest:
    """
    Attributes:
        metrics (List['MetricName']):
        timezone (Union[Unset, str]): Type format Iana timezone
        return_unit (Union[Unset, bool]):
    """

    metrics: List["MetricName"]
    timezone: Union[Unset, str] = UNSET
    return_unit: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        metrics = []
        for metrics_item_data in self.metrics:
            metrics_item = metrics_item_data.to_dict()
            metrics.append(metrics_item)

        timezone = self.timezone

        return_unit = self.return_unit

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "metrics": metrics,
            }
        )
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if return_unit is not UNSET:
            field_dict["returnUnit"] = return_unit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.metric_name import MetricName

        d = src_dict.copy()
        metrics = []
        _metrics = d.pop("metrics")
        for metrics_item_data in _metrics:
            metrics_item = MetricName.from_dict(metrics_item_data)

            metrics.append(metrics_item)

        timezone = d.pop("timezone", UNSET)

        return_unit = d.pop("returnUnit", UNSET)

        latest = cls(
            metrics=metrics,
            timezone=timezone,
            return_unit=return_unit,
        )

        return latest
