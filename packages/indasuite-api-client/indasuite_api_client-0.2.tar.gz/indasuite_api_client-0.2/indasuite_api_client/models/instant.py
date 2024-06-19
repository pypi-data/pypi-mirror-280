import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.instant_query_direction import InstantQueryDirection
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metric_name import MetricName


T = TypeVar("T", bound="Instant")


@_attrs_define
class Instant:
    """
    Attributes:
        moment (datetime.datetime):
        metrics (List['MetricName']):
        query_direction (Union[Unset, InstantQueryDirection]):
        timezone (Union[Unset, str]): Type format Iana timezone
    """

    moment: datetime.datetime
    metrics: List["MetricName"]
    query_direction: Union[Unset, InstantQueryDirection] = UNSET
    timezone: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        moment = self.moment.isoformat()

        metrics = []
        for metrics_item_data in self.metrics:
            metrics_item = metrics_item_data.to_dict()
            metrics.append(metrics_item)

        query_direction: Union[Unset, str] = UNSET
        if not isinstance(self.query_direction, Unset):
            query_direction = self.query_direction.value

        timezone = self.timezone

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "moment": moment,
                "metrics": metrics,
            }
        )
        if query_direction is not UNSET:
            field_dict["queryDirection"] = query_direction
        if timezone is not UNSET:
            field_dict["timezone"] = timezone

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.metric_name import MetricName

        d = src_dict.copy()
        moment = isoparse(d.pop("moment"))

        metrics = []
        _metrics = d.pop("metrics")
        for metrics_item_data in _metrics:
            metrics_item = MetricName.from_dict(metrics_item_data)

            metrics.append(metrics_item)

        _query_direction = d.pop("queryDirection", UNSET)
        query_direction: Union[Unset, InstantQueryDirection]
        if isinstance(_query_direction, Unset):
            query_direction = UNSET
        else:
            query_direction = InstantQueryDirection(_query_direction)

        timezone = d.pop("timezone", UNSET)

        instant = cls(
            moment=moment,
            metrics=metrics,
            query_direction=query_direction,
            timezone=timezone,
        )

        return instant
