import datetime
from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define
from dateutil.parser import isoparse

T = TypeVar("T", bound="DeleteMetricValues")


@_attrs_define
class DeleteMetricValues:
    """
    Attributes:
        name (str):
        start (datetime.datetime):
        end (datetime.datetime):
    """

    name: str
    start: datetime.datetime
    end: datetime.datetime

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        start = self.start.isoformat()

        end = self.end.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
                "start": start,
                "end": end,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        start = isoparse(d.pop("start"))

        end = isoparse(d.pop("end"))

        delete_metric_values = cls(
            name=name,
            start=start,
            end=end,
        )

        return delete_metric_values
