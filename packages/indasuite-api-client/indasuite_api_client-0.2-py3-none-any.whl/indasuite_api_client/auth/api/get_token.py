from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import TokenClient
from ...models.error_response import ErrorResponse
from ..models import ResponseWithToken
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client_id: Union[Unset, str] = UNSET,
    client_secret: Union[Unset, str] = UNSET,
    audience: Union[Unset, str] = UNSET,
    grant_type: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:

    content: Dict[str, Any] = {}

    content["client_id"] = client_id
    content["client_secret"] = client_secret
    content["audience"] = audience
    content["grant_type"] = grant_type

    content = {k: v for k, v in content.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "",
        "headers": {"Content-Type": "application/json"},
        "json": content,
    }

    return _kwargs


def _parse_response(
    *, client: TokenClient, response: httpx.Response
) -> Optional[Union[ErrorResponse, ResponseWithToken]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ResponseWithToken.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: TokenClient, response: httpx.Response
) -> Response[Union[ErrorResponse, ResponseWithToken]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: TokenClient,
) -> Response[Union[ErrorResponse, ResponseWithToken]]:
    """Get authentification token

    Args:
        client (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, ResponseWithToken]]
    """

    kwargs = _get_kwargs(
        client_id=client.client_id,
        client_secret=client.client_secret,
        audience=client.audience,
        grant_type=client.grant_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: TokenClient,
) -> Optional[Union[ErrorResponse, ResponseWithToken]]:
    """Get authentification token

    Args:
        client (Union[Unset, str]):
        client_id (Union[Unset, str]):
        client_secret (Union[Unset, str]):
        audience (Union[Unset, str]):
        grant_type (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, ResponseWithMetricList]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: TokenClient,
) -> Response[Union[ErrorResponse, ResponseWithToken]]:
    """Get list of metrics

    Args:
        client (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, ResponseWithToken]]
    """

    kwargs = _get_kwargs(
        client_id=client.client_id,
        client_secret=client.client_secret,
        audience=client.audience,
        grant_type=client.grant_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: TokenClient,
) -> Optional[Union[ErrorResponse, ResponseWithToken]]:
    """Get list of metrics

    Args:
        client (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, ResponseWithToken]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
