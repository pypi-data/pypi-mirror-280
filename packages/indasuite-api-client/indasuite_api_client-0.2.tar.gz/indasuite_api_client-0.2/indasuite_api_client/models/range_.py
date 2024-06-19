import datetime
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metric_name import MetricName


T = TypeVar("T", bound="Range")


@_attrs_define
class Range:
    """
    Attributes:
        start (datetime.datetime):
        end (datetime.datetime):
        metric (MetricName):
        timezone (Union[Unset, str]): Type format Iana timezone
        limit (Union[Unset, int]):
        show_annotation (Union[Unset, bool]):
        aggregation (Union[Unset, Any]):
        filter_ (Union[Unset, str]):
    """

    start: datetime.datetime
    end: datetime.datetime
    metric: "MetricName"
    timezone: Union[Unset, str] = UNSET
    limit: Union[Unset, int] = UNSET
    show_annotation: Union[Unset, bool] = UNSET
    aggregation: Union[Unset, Any] = UNSET
    filter_: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        start = self.start.isoformat()

        end = self.end.isoformat()

        metric = self.metric.to_dict()

        timezone = self.timezone

        limit = self.limit

        show_annotation = self.show_annotation

        aggregation = self.aggregation

        filter_ = self.filter_

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "start": start,
                "end": end,
                "metric": metric,
            }
        )
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if limit is not UNSET:
            field_dict["limit"] = limit
        if show_annotation is not UNSET:
            field_dict["showAnnotation"] = show_annotation
        if aggregation is not UNSET:
            field_dict["aggregation"] = aggregation
        if filter_ is not UNSET:
            field_dict["filter"] = filter_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.metric_name import MetricName

        d = src_dict.copy()
        start = isoparse(d.pop("start"))

        end = isoparse(d.pop("end"))

        metric = MetricName.from_dict(d.pop("metric"))

        timezone = d.pop("timezone", UNSET)

        limit = d.pop("limit", UNSET)

        show_annotation = d.pop("showAnnotation", UNSET)

        aggregation = d.pop("aggregation", UNSET)

        filter_ = d.pop("filter", UNSET)

        range_ = cls(
            start=start,
            end=end,
            metric=metric,
            timezone=timezone,
            limit=limit,
            show_annotation=show_annotation,
            aggregation=aggregation,
            filter_=filter_,
        )

        return range_
