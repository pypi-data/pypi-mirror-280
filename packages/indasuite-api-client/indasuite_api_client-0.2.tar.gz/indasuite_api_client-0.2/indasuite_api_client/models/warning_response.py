from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.api_status_code import ApiStatusCode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error import Error


T = TypeVar("T", bound="WarningResponse")


@_attrs_define
class WarningResponse:
    """
    Attributes:
        status_code (Union[Unset, ApiStatusCode]): Members:
            |Value|Description|
            |---|---|
            |1010|OK|
            |1020|Error from database engine|
            |1021|Invalid datasource name|
            |1022|Out of range timestamp|
            |1050|Invalid request|
            |1060|Annotation point was not found|
            |1300|Metric already exist|
            |1301|Metric update failed|
            |1302|Formula metric type mismatch|
            |1303|Changing metric type is not allowed|
            |1305|Name already exists|
            |1310|Default access zone cannot be created/updated/deleted|
            |1350|User already exist in access zone|
            |1360|Invalid file format|
            |1400|Unidentified error|
            |1403|Invalid Authorization|
            |1404|At least one metric is forbidden by permission|
            |1405|At least one of the specified timestamps is in the future|
            |1406|At least one invalid metric name|
            |1500|Internal server error|
            |1501|Warning|
            |1502|Unable to decompress payload|
            |1503|Invalid header content encoding|
        message (Union[Unset, str]):
        errors (Union[List['Error'], None, Unset]):
        success (Union[None, Unset, int]):
        fails (Union[None, Unset, int]):
    """

    status_code: Union[Unset, ApiStatusCode] = UNSET
    message: Union[Unset, str] = UNSET
    errors: Union[List["Error"], None, Unset] = UNSET
    success: Union[None, Unset, int] = UNSET
    fails: Union[None, Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        status_code: Union[Unset, int] = UNSET
        if not isinstance(self.status_code, Unset):
            status_code = self.status_code.value

        message = self.message

        errors: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.errors, Unset):
            errors = UNSET
        elif isinstance(self.errors, list):
            errors = []
            for errors_type_0_item_data in self.errors:
                errors_type_0_item = errors_type_0_item_data.to_dict()
                errors.append(errors_type_0_item)

        else:
            errors = self.errors

        success: Union[None, Unset, int]
        if isinstance(self.success, Unset):
            success = UNSET
        else:
            success = self.success

        fails: Union[None, Unset, int]
        if isinstance(self.fails, Unset):
            fails = UNSET
        else:
            fails = self.fails

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if status_code is not UNSET:
            field_dict["statusCode"] = status_code
        if message is not UNSET:
            field_dict["message"] = message
        if errors is not UNSET:
            field_dict["errors"] = errors
        if success is not UNSET:
            field_dict["success"] = success
        if fails is not UNSET:
            field_dict["fails"] = fails

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.error import Error

        d = src_dict.copy()
        _status_code = d.pop("statusCode", UNSET)
        status_code: Union[Unset, ApiStatusCode]
        if isinstance(_status_code, Unset):
            status_code = UNSET
        else:
            status_code = ApiStatusCode(_status_code)

        message = d.pop("message", UNSET)

        def _parse_errors(data: object) -> Union[List["Error"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                errors_type_0 = []
                _errors_type_0 = data
                for errors_type_0_item_data in _errors_type_0:
                    errors_type_0_item = Error.from_dict(errors_type_0_item_data)

                    errors_type_0.append(errors_type_0_item)

                return errors_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["Error"], None, Unset], data)

        errors = _parse_errors(d.pop("errors", UNSET))

        def _parse_success(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        success = _parse_success(d.pop("success", UNSET))

        def _parse_fails(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        fails = _parse_fails(d.pop("fails", UNSET))

        warning_response = cls(
            status_code=status_code,
            message=message,
            errors=errors,
            success=success,
            fails=fails,
        )

        return warning_response
