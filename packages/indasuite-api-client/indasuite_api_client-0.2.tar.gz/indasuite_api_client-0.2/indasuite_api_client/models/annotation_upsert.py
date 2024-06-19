import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AnnotationUpsert")


@_attrs_define
class AnnotationUpsert:
    """
    Attributes:
        name (str):
        timestamp (datetime.datetime):
        annotation (Union[Unset, str]):
    """

    name: str
    timestamp: datetime.datetime
    annotation: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        timestamp = self.timestamp.isoformat()

        annotation = self.annotation

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
                "timestamp": timestamp,
            }
        )
        if annotation is not UNSET:
            field_dict["annotation"] = annotation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        timestamp = isoparse(d.pop("timestamp"))

        annotation = d.pop("annotation", UNSET)

        annotation_upsert = cls(
            name=name,
            timestamp=timestamp,
            annotation=annotation,
        )

        return annotation_upsert
