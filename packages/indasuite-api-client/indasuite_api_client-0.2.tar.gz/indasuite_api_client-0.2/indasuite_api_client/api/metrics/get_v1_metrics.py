from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.response_with_metric_list import ResponseWithMetricList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    name: Union[Unset, str] = UNSET,
    datasource: Union[Unset, str] = UNSET,
    only_formula: Union[Unset, bool] = False,
    access_zone_id: Union[Unset, str] = UNSET,
    pagination_key: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 50,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["name"] = name

    params["datasource"] = datasource

    params["onlyFormula"] = only_formula

    params["accessZoneId"] = access_zone_id

    params["paginationKey"] = pagination_key

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v1/metrics",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, ResponseWithMetricList]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ResponseWithMetricList.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, ResponseWithMetricList]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    name: Union[Unset, str] = UNSET,
    datasource: Union[Unset, str] = UNSET,
    only_formula: Union[Unset, bool] = False,
    access_zone_id: Union[Unset, str] = UNSET,
    pagination_key: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 50,
) -> Response[Union[ErrorResponse, ResponseWithMetricList]]:
    """Get list of metrics

    Args:
        name (Union[Unset, str]):
        datasource (Union[Unset, str]):
        only_formula (Union[Unset, bool]):  Default: False.
        access_zone_id (Union[Unset, str]):
        pagination_key (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, ResponseWithMetricList]]
    """

    kwargs = _get_kwargs(
        name=name,
        datasource=datasource,
        only_formula=only_formula,
        access_zone_id=access_zone_id,
        pagination_key=pagination_key,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    name: Union[Unset, str] = UNSET,
    datasource: Union[Unset, str] = UNSET,
    only_formula: Union[Unset, bool] = False,
    access_zone_id: Union[Unset, str] = UNSET,
    pagination_key: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 50,
) -> Optional[Union[ErrorResponse, ResponseWithMetricList]]:
    """Get list of metrics

    Args:
        name (Union[Unset, str]):
        datasource (Union[Unset, str]):
        only_formula (Union[Unset, bool]):  Default: False.
        access_zone_id (Union[Unset, str]):
        pagination_key (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, ResponseWithMetricList]
    """

    return sync_detailed(
        client=client,
        name=name,
        datasource=datasource,
        only_formula=only_formula,
        access_zone_id=access_zone_id,
        pagination_key=pagination_key,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    name: Union[Unset, str] = UNSET,
    datasource: Union[Unset, str] = UNSET,
    only_formula: Union[Unset, bool] = False,
    access_zone_id: Union[Unset, str] = UNSET,
    pagination_key: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 50,
) -> Response[Union[ErrorResponse, ResponseWithMetricList]]:
    """Get list of metrics

    Args:
        name (Union[Unset, str]):
        datasource (Union[Unset, str]):
        only_formula (Union[Unset, bool]):  Default: False.
        access_zone_id (Union[Unset, str]):
        pagination_key (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, ResponseWithMetricList]]
    """

    kwargs = _get_kwargs(
        name=name,
        datasource=datasource,
        only_formula=only_formula,
        access_zone_id=access_zone_id,
        pagination_key=pagination_key,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    name: Union[Unset, str] = UNSET,
    datasource: Union[Unset, str] = UNSET,
    only_formula: Union[Unset, bool] = False,
    access_zone_id: Union[Unset, str] = UNSET,
    pagination_key: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 50,
) -> Optional[Union[ErrorResponse, ResponseWithMetricList]]:
    """Get list of metrics

    Args:
        name (Union[Unset, str]):
        datasource (Union[Unset, str]):
        only_formula (Union[Unset, bool]):  Default: False.
        access_zone_id (Union[Unset, str]):
        pagination_key (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, ResponseWithMetricList]
    """

    return (
        await asyncio_detailed(
            client=client,
            name=name,
            datasource=datasource,
            only_formula=only_formula,
            access_zone_id=access_zone_id,
            pagination_key=pagination_key,
            limit=limit,
        )
    ).parsed
