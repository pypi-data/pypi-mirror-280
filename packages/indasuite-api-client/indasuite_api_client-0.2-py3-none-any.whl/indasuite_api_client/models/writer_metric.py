from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.writer_metric_data import WriterMetricData


T = TypeVar("T", bound="WriterMetric")


@_attrs_define
class WriterMetric:
    """
    Attributes:
        name (str):
        values (List['WriterMetricData']):
    """

    name: str
    values: List["WriterMetricData"]

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        values = []
        for values_item_data in self.values:
            values_item = values_item_data.to_dict()
            values.append(values_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
                "values": values,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.writer_metric_data import WriterMetricData

        d = src_dict.copy()
        name = d.pop("name")

        values = []
        _values = d.pop("values")
        for values_item_data in _values:
            values_item = WriterMetricData.from_dict(values_item_data)

            values.append(values_item)

        writer_metric = cls(
            name=name,
            values=values,
        )

        return writer_metric
