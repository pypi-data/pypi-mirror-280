import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.annotation import Annotation


T = TypeVar("T", bound="MetricDataWithAnnotations")


@_attrs_define
class MetricDataWithAnnotations:
    """
    Attributes:
        timestamp (Union[Unset, datetime.datetime]):
        value (Union[Unset, Any]):
        annotations (Union[List['Annotation'], None, Unset]):
    """

    timestamp: Union[Unset, datetime.datetime] = UNSET
    value: Union[Unset, Any] = UNSET
    annotations: Union[List["Annotation"], None, Unset] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        value = self.value

        annotations: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.annotations, Unset):
            annotations = UNSET
        elif isinstance(self.annotations, list):
            annotations = []
            for annotations_type_0_item_data in self.annotations:
                annotations_type_0_item = annotations_type_0_item_data.to_dict()
                annotations.append(annotations_type_0_item)

        else:
            annotations = self.annotations

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if value is not UNSET:
            field_dict["value"] = value
        if annotations is not UNSET:
            field_dict["annotations"] = annotations

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.annotation import Annotation

        d = src_dict.copy()
        _timestamp = d.pop("timestamp", UNSET)
        timestamp: Union[Unset, datetime.datetime]
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)

        value = d.pop("value", UNSET)

        def _parse_annotations(data: object) -> Union[List["Annotation"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                annotations_type_0 = []
                _annotations_type_0 = data
                for annotations_type_0_item_data in _annotations_type_0:
                    annotations_type_0_item = Annotation.from_dict(annotations_type_0_item_data)

                    annotations_type_0.append(annotations_type_0_item)

                return annotations_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["Annotation"], None, Unset], data)

        annotations = _parse_annotations(d.pop("annotations", UNSET))

        metric_data_with_annotations = cls(
            timestamp=timestamp,
            value=value,
            annotations=annotations,
        )

        return metric_data_with_annotations
