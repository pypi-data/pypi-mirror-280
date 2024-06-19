from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.api_status_code import ApiStatusCode
from ..types import UNSET, Unset

T = TypeVar("T", bound="ResponseWithDatabaseList")


@_attrs_define
class ResponseWithDatabaseList:
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
        data (Union[List[str], None, Unset]):
    """

    status_code: Union[Unset, ApiStatusCode] = UNSET
    message: Union[Unset, str] = UNSET
    data: Union[List[str], None, Unset] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        status_code: Union[Unset, int] = UNSET
        if not isinstance(self.status_code, Unset):
            status_code = self.status_code.value

        message = self.message

        data: Union[List[str], None, Unset]
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, list):
            data = self.data

        else:
            data = self.data

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if status_code is not UNSET:
            field_dict["statusCode"] = status_code
        if message is not UNSET:
            field_dict["message"] = message
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _status_code = d.pop("statusCode", UNSET)
        status_code: Union[Unset, ApiStatusCode]
        if isinstance(_status_code, Unset):
            status_code = UNSET
        else:
            status_code = ApiStatusCode(_status_code)

        message = d.pop("message", UNSET)

        def _parse_data(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                data_type_0 = cast(List[str], data)

                return data_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        data = _parse_data(d.pop("data", UNSET))

        response_with_database_list = cls(
            status_code=status_code,
            message=message,
            data=data,
        )

        return response_with_database_list
