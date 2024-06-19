from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metric_data_with_annotations import MetricDataWithAnnotations


T = TypeVar("T", bound="ResponseWithMetricDataWithAnnotationsList")


@_attrs_define
class ResponseWithMetricDataWithAnnotationsList:
    """
    Attributes:
        is_response_complete (Union[None, Unset, bool]):
        name (Union[Unset, str]):
        unit (Union[Unset, str]):
        values (Union[List['MetricDataWithAnnotations'], None, Unset]):
    """

    is_response_complete: Union[None, Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    unit: Union[Unset, str] = UNSET
    values: Union[List["MetricDataWithAnnotations"], None, Unset] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        is_response_complete: Union[None, Unset, bool]
        if isinstance(self.is_response_complete, Unset):
            is_response_complete = UNSET
        else:
            is_response_complete = self.is_response_complete

        name = self.name

        unit = self.unit

        values: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.values, Unset):
            values = UNSET
        elif isinstance(self.values, list):
            values = []
            for values_type_0_item_data in self.values:
                values_type_0_item = values_type_0_item_data.to_dict()
                values.append(values_type_0_item)

        else:
            values = self.values

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if is_response_complete is not UNSET:
            field_dict["isResponseComplete"] = is_response_complete
        if name is not UNSET:
            field_dict["name"] = name
        if unit is not UNSET:
            field_dict["unit"] = unit
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.metric_data_with_annotations import MetricDataWithAnnotations

        d = src_dict.copy()

        def _parse_is_response_complete(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_response_complete = _parse_is_response_complete(d.pop("isResponseComplete", UNSET))

        name = d.pop("name", UNSET)

        unit = d.pop("unit", UNSET)

        def _parse_values(data: object) -> Union[List["MetricDataWithAnnotations"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                values_type_0 = []
                _values_type_0 = data
                for values_type_0_item_data in _values_type_0:
                    values_type_0_item = MetricDataWithAnnotations.from_dict(values_type_0_item_data)

                    values_type_0.append(values_type_0_item)

                return values_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["MetricDataWithAnnotations"], None, Unset], data)

        values = _parse_values(d.pop("values", UNSET))

        response_with_metric_data_with_annotations_list = cls(
            is_response_complete=is_response_complete,
            name=name,
            unit=unit,
            values=values,
        )

        return response_with_metric_data_with_annotations_list
