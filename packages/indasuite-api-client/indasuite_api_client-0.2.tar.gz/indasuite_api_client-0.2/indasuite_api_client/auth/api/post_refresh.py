from http import HTTPStatus
import logging
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import RefreshTokenClient
from ..models.error import Error
from ..models.message import Message
from ..models.refresh_token_request import RefreshTokenRequest
from ..models.token_response import TokenResponse
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        RefreshTokenRequest,
        RefreshTokenRequest,
    ],
    api_key,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/refresh",
    }

    if isinstance(body, RefreshTokenRequest):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, RefreshTokenRequest):
        _data_body = body.to_dict()

        _kwargs["data"] = _data_body
        headers["Content-Type"] = "application/x-www-form-urlencoded"

    headers["x-api-key"] = api_key

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: RefreshTokenClient, response: httpx.Response
) -> Optional[Union[TokenResponse, Union["Error", "Message"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = TokenResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.FORBIDDEN:

        def _parse_response_403(data: object) -> Union["Error", "Message"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_403_type_0 = Message.from_dict(data)

                return response_403_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_403_type_1 = Error.from_dict(data)

            return response_403_type_1

        response_403 = _parse_response_403(response.json())

        return response_403
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: RefreshTokenClient, response: httpx.Response
) -> Response[Union[TokenResponse, Union["Error", "Message"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: RefreshTokenClient,
    body: Union[
        RefreshTokenRequest,
        RefreshTokenRequest,
    ],
) -> Response[Union[TokenResponse, Union["Error", "Message"]]]:
    """Refreshes a token for a device

    Args:
        body (RefreshTokenRequest):
        body (RefreshTokenRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[TokenResponse, Union['Error', 'Message']]]
    """

    kwargs = _get_kwargs(
        body=body,
        api_key=client.api_key,
    )
    logging.debug(f"Refresh kwargs : {kwargs}")

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: RefreshTokenClient,
    body: Union[
        RefreshTokenRequest,
        RefreshTokenRequest,
    ],
) -> Optional[Union[TokenResponse, Union["Error", "Message"]]]:
    """Refreshes a token for a device

    Args:
        body (RefreshTokenRequest):
        body (RefreshTokenRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[TokenResponse, Union['Error', 'Message']]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: RefreshTokenClient,
    body: Union[
        RefreshTokenRequest,
        RefreshTokenRequest,
    ],
) -> Response[Union[TokenResponse, Union["Error", "Message"]]]:
    """Refreshes a token for a device

    Args:
        body (RefreshTokenRequest):
        body (RefreshTokenRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[TokenResponse, Union['Error', 'Message']]]
    """

    kwargs = _get_kwargs(
        body=body,
        x_api_key=client.x_api_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: RefreshTokenClient,
    body: Union[
        RefreshTokenRequest,
        RefreshTokenRequest,
    ],
) -> Optional[Union[TokenResponse, Union["Error", "Message"]]]:
    """Refreshes a token for a device

    Args:
        body (RefreshTokenRequest):
        body (RefreshTokenRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[TokenResponse, Union['Error', 'Message']]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
