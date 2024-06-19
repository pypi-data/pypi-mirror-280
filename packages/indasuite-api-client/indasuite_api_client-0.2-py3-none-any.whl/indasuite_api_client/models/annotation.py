import datetime
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.annotation_value_update import AnnotationValueUpdate


T = TypeVar("T", bound="Annotation")


@_attrs_define
class Annotation:
    """
    Attributes:
        id (Union[Unset, str]):
        timestamp (Union[Unset, datetime.datetime]):
        value (Union[Unset, str]):
        is_author (Union[Unset, bool]):
        value_update (Union[Unset, AnnotationValueUpdate]):
        user_name (Union[Unset, str]):
        created (Union[Unset, datetime.datetime]):
    """

    id: Union[Unset, str] = UNSET
    timestamp: Union[Unset, datetime.datetime] = UNSET
    value: Union[Unset, str] = UNSET
    is_author: Union[Unset, bool] = UNSET
    value_update: Union[Unset, "AnnotationValueUpdate"] = UNSET
    user_name: Union[Unset, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        value = self.value

        is_author = self.is_author

        value_update: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.value_update, Unset):
            value_update = self.value_update.to_dict()

        user_name = self.user_name

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if value is not UNSET:
            field_dict["value"] = value
        if is_author is not UNSET:
            field_dict["isAuthor"] = is_author
        if value_update is not UNSET:
            field_dict["valueUpdate"] = value_update
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if created is not UNSET:
            field_dict["created"] = created

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.annotation_value_update import AnnotationValueUpdate

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: Union[Unset, datetime.datetime]
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)

        value = d.pop("value", UNSET)

        is_author = d.pop("isAuthor", UNSET)

        _value_update = d.pop("valueUpdate", UNSET)
        value_update: Union[Unset, AnnotationValueUpdate]
        if isinstance(_value_update, Unset):
            value_update = UNSET
        else:
            value_update = AnnotationValueUpdate.from_dict(_value_update)

        user_name = d.pop("userName", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        annotation = cls(
            id=id,
            timestamp=timestamp,
            value=value,
            is_author=is_author,
            value_update=value_update,
            user_name=user_name,
            created=created,
        )

        return annotation
