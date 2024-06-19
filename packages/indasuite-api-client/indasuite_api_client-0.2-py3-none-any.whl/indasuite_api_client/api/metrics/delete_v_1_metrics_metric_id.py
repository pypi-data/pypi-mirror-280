from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.ok_response import OkResponse
from ...types import Response


def _get_kwargs(
    metric_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": f"/v1/metrics/{metric_id}",
    }

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
    metric_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[ErrorResponse, OkResponse]]:
    """Completely delete metric

     API custom return codes :
    1050 - Invalid request
    1400 - Unidentified error

    Args:
        metric_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, OkResponse]]
    """

    kwargs = _get_kwargs(
        metric_id=metric_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    metric_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorResponse, OkResponse]]:
    """Completely delete metric

     API custom return codes :
    1050 - Invalid request
    1400 - Unidentified error

    Args:
        metric_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, OkResponse]
    """

    return sync_detailed(
        metric_id=metric_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    metric_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[ErrorResponse, OkResponse]]:
    """Completely delete metric

     API custom return codes :
    1050 - Invalid request
    1400 - Unidentified error

    Args:
        metric_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, OkResponse]]
    """

    kwargs = _get_kwargs(
        metric_id=metric_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    metric_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorResponse, OkResponse]]:
    """Completely delete metric

     API custom return codes :
    1050 - Invalid request
    1400 - Unidentified error

    Args:
        metric_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, OkResponse]
    """

    return (
        await asyncio_detailed(
            metric_id=metric_id,
            client=client,
        )
    ).parsed
