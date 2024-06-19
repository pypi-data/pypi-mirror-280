from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="WriterMetadata")


@_attrs_define
class WriterMetadata:
    """
    Attributes:
        site (Union[Unset, str]):
        device (Union[Unset, str]):
        prefix (Union[Unset, str]):
    """

    site: Union[Unset, str] = UNSET
    device: Union[Unset, str] = UNSET
    prefix: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        site = self.site

        device = self.device

        prefix = self.prefix

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if site is not UNSET:
            field_dict["site"] = site
        if device is not UNSET:
            field_dict["device"] = device
        if prefix is not UNSET:
            field_dict["prefix"] = prefix

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        site = d.pop("site", UNSET)

        device = d.pop("device", UNSET)

        prefix = d.pop("prefix", UNSET)

        writer_metadata = cls(
            site=site,
            device=device,
            prefix=prefix,
        )

        return writer_metadata
