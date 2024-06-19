import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="MetricData")


@_attrs_define
class MetricData:
    """
    Attributes:
        timestamp (Union[Unset, datetime.datetime]):
        value (Union[Unset, Any]):
    """

    timestamp: Union[Unset, datetime.datetime] = UNSET
    value: Union[Unset, Any] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _timestamp = d.pop("timestamp", UNSET)
        timestamp: Union[Unset, datetime.datetime]
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)

        value = d.pop("value", UNSET)

        metric_data = cls(
            timestamp=timestamp,
            value=value,
        )

        return metric_data
