from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.range_ import Range
from ...models.response_with_metric_data_with_annotations_list import ResponseWithMetricDataWithAnnotationsList
from ...types import Response


def _get_kwargs(
    datasource: str,
    *,
    body: Union[
        Range,
        Range,
        Range,
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/v1/databases/{datasource}/query/range",
    }

    if isinstance(body, Range):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, Range):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "text/json"
    if isinstance(body, Range):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, ResponseWithMetricDataWithAnnotationsList]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ResponseWithMetricDataWithAnnotationsList.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, ResponseWithMetricDataWithAnnotationsList]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    datasource: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        Range,
        Range,
        Range,
    ],
) -> Response[Union[ErrorResponse, ResponseWithMetricDataWithAnnotationsList]]:
    """Retrieve metric values for a given time serie and time range.

     API custom return codes :
    1020 - Error from database engine
    1050 - Invalid request

    Args:
        datasource (str):
        body (Range):
        body (Range):
        body (Range):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, ResponseWithMetricDataWithAnnotationsList]]
    """

    kwargs = _get_kwargs(
        datasource=datasource,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    datasource: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        Range,
        Range,
        Range,
    ],
) -> Optional[Union[ErrorResponse, ResponseWithMetricDataWithAnnotationsList]]:
    """Retrieve metric values for a given time serie and time range.

     API custom return codes :
    1020 - Error from database engine
    1050 - Invalid request

    Args:
        datasource (str):
        body (Range):
        body (Range):
        body (Range):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, ResponseWithMetricDataWithAnnotationsList]
    """

    return sync_detailed(
        datasource=datasource,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    datasource: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        Range,
        Range,
        Range,
    ],
) -> Response[Union[ErrorResponse, ResponseWithMetricDataWithAnnotationsList]]:
    """Retrieve metric values for a given time serie and time range.

     API custom return codes :
    1020 - Error from database engine
    1050 - Invalid request

    Args:
        datasource (str):
        body (Range):
        body (Range):
        body (Range):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, ResponseWithMetricDataWithAnnotationsList]]
    """

    kwargs = _get_kwargs(
        datasource=datasource,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    datasource: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        Range,
        Range,
        Range,
    ],
) -> Optional[Union[ErrorResponse, ResponseWithMetricDataWithAnnotationsList]]:
    """Retrieve metric values for a given time serie and time range.

     API custom return codes :
    1020 - Error from database engine
    1050 - Invalid request

    Args:
        datasource (str):
        body (Range):
        body (Range):
        body (Range):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, ResponseWithMetricDataWithAnnotationsList]
    """

    return (
        await asyncio_detailed(
            datasource=datasource,
            client=client,
            body=body,
        )
    ).parsed
