from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.writer_metadata import WriterMetadata
    from ..models.writer_metric import WriterMetric


T = TypeVar("T", bound="Writer")


@_attrs_define
class Writer:
    """
    Attributes:
        body (List['WriterMetric']):
        metadata (Union[Unset, WriterMetadata]):
    """

    body: List["WriterMetric"]
    metadata: Union[Unset, "WriterMetadata"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        body = []
        for body_item_data in self.body:
            body_item = body_item_data.to_dict()
            body.append(body_item)

        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "body": body,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.writer_metadata import WriterMetadata
        from ..models.writer_metric import WriterMetric

        d = src_dict.copy()
        body = []
        _body = d.pop("body")
        for body_item_data in _body:
            body_item = WriterMetric.from_dict(body_item_data)

            body.append(body_item)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, WriterMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = WriterMetadata.from_dict(_metadata)

        writer = cls(
            body=body,
            metadata=metadata,
        )

        return writer
