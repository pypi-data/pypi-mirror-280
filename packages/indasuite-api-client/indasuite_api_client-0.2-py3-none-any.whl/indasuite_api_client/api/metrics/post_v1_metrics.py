from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.metric_upset import MetricUpset
from ...models.response_with_metric import ResponseWithMetric
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        MetricUpset,
        MetricUpset,
        MetricUpset,
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/v1/metrics",
    }

    if isinstance(body, MetricUpset):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, MetricUpset):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "text/json"
    if isinstance(body, MetricUpset):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, ResponseWithMetric]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ResponseWithMetric.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, ResponseWithMetric]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        MetricUpset,
        MetricUpset,
        MetricUpset,
    ],
) -> Response[Union[ErrorResponse, ResponseWithMetric]]:
    """Add new metric

     API custom return codes :
    1021 - Invalid datasource name
    1050 - Invalid request
    1300 - Metric already exist
    1302 - Formula metric type mismatch
    1400 - Unidentified error

    Args:
        body (MetricUpset):
        body (MetricUpset):
        body (MetricUpset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, ResponseWithMetric]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: Union[
        MetricUpset,
        MetricUpset,
        MetricUpset,
    ],
) -> Optional[Union[ErrorResponse, ResponseWithMetric]]:
    """Add new metric

     API custom return codes :
    1021 - Invalid datasource name
    1050 - Invalid request
    1300 - Metric already exist
    1302 - Formula metric type mismatch
    1400 - Unidentified error

    Args:
        body (MetricUpset):
        body (MetricUpset):
        body (MetricUpset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, ResponseWithMetric]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        MetricUpset,
        MetricUpset,
        MetricUpset,
    ],
) -> Response[Union[ErrorResponse, ResponseWithMetric]]:
    """Add new metric

     API custom return codes :
    1021 - Invalid datasource name
    1050 - Invalid request
    1300 - Metric already exist
    1302 - Formula metric type mismatch
    1400 - Unidentified error

    Args:
        body (MetricUpset):
        body (MetricUpset):
        body (MetricUpset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, ResponseWithMetric]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: Union[
        MetricUpset,
        MetricUpset,
        MetricUpset,
    ],
) -> Optional[Union[ErrorResponse, ResponseWithMetric]]:
    """Add new metric

     API custom return codes :
    1021 - Invalid datasource name
    1050 - Invalid request
    1300 - Metric already exist
    1302 - Formula metric type mismatch
    1400 - Unidentified error

    Args:
        body (MetricUpset):
        body (MetricUpset):
        body (MetricUpset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, ResponseWithMetric]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
