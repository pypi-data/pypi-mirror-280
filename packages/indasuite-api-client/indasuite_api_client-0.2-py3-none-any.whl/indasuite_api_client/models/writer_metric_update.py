from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.writer_metric_data import WriterMetricData


T = TypeVar("T", bound="WriterMetricUpdate")


@_attrs_define
class WriterMetricUpdate:
    """
    Attributes:
        name (str):
        value (WriterMetricData):
        message (Union[Unset, str]):
    """

    name: str
    value: "WriterMetricData"
    message: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        value = self.value.to_dict()

        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
                "value": value,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.writer_metric_data import WriterMetricData

        d = src_dict.copy()
        name = d.pop("name")

        value = WriterMetricData.from_dict(d.pop("value"))

        message = d.pop("message", UNSET)

        writer_metric_update = cls(
            name=name,
            value=value,
            message=message,
        )

        return writer_metric_update
