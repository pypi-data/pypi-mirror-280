from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_metric_values import DeleteMetricValues
from ...models.error_response import ErrorResponse
from ...models.ok_response import OkResponse
from ...types import Response


def _get_kwargs(
    datasource: str,
    *,
    body: Union[
        DeleteMetricValues,
        DeleteMetricValues,
        DeleteMetricValues,
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": f"/v1/databases/{datasource}/values",
    }

    if isinstance(body, DeleteMetricValues):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, DeleteMetricValues):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "text/json"
    if isinstance(body, DeleteMetricValues):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, OkResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = OkResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, OkResponse]]:
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
        DeleteMetricValues,
        DeleteMetricValues,
        DeleteMetricValues,
    ],
) -> Response[Union[ErrorResponse, OkResponse]]:
    """Delete values into measurement with datetime

     API custom return codes :
    1021 - Invalid datasource name
    1050 - Invalid request

    Args:
        datasource (str):
        body (DeleteMetricValues):
        body (DeleteMetricValues):
        body (DeleteMetricValues):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, OkResponse]]
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
        DeleteMetricValues,
        DeleteMetricValues,
        DeleteMetricValues,
    ],
) -> Optional[Union[ErrorResponse, OkResponse]]:
    """Delete values into measurement with datetime

     API custom return codes :
    1021 - Invalid datasource name
    1050 - Invalid request

    Args:
        datasource (str):
        body (DeleteMetricValues):
        body (DeleteMetricValues):
        body (DeleteMetricValues):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, OkResponse]
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
        DeleteMetricValues,
        DeleteMetricValues,
        DeleteMetricValues,
    ],
) -> Response[Union[ErrorResponse, OkResponse]]:
    """Delete values into measurement with datetime

     API custom return codes :
    1021 - Invalid datasource name
    1050 - Invalid request

    Args:
        datasource (str):
        body (DeleteMetricValues):
        body (DeleteMetricValues):
        body (DeleteMetricValues):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, OkResponse]]
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
        DeleteMetricValues,
        DeleteMetricValues,
        DeleteMetricValues,
    ],
) -> Optional[Union[ErrorResponse, OkResponse]]:
    """Delete values into measurement with datetime

     API custom return codes :
    1021 - Invalid datasource name
    1050 - Invalid request

    Args:
        datasource (str):
        body (DeleteMetricValues):
        body (DeleteMetricValues):
        body (DeleteMetricValues):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, OkResponse]
    """

    return (
        await asyncio_detailed(
            datasource=datasource,
            client=client,
            body=body,
        )
    ).parsed
