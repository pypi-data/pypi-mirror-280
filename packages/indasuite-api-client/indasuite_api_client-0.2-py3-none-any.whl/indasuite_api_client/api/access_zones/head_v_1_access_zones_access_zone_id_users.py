from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bad_request_result import BadRequestResult
from ...models.not_found_result import NotFoundResult
from ...models.ok_result import OkResult
from ...types import Response


def _get_kwargs(
    access_zone_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "head",
        "url": f"/v1/access-zones/{access_zone_id}/users",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[BadRequestResult, NotFoundResult, OkResult]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = OkResult.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = BadRequestResult.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = NotFoundResult.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[BadRequestResult, NotFoundResult, OkResult]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    access_zone_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[BadRequestResult, NotFoundResult, OkResult]]:
    """Check if the user is present in the access zone.

    Args:
        access_zone_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequestResult, NotFoundResult, OkResult]]
    """

    kwargs = _get_kwargs(
        access_zone_id=access_zone_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    access_zone_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[BadRequestResult, NotFoundResult, OkResult]]:
    """Check if the user is present in the access zone.

    Args:
        access_zone_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequestResult, NotFoundResult, OkResult]
    """

    return sync_detailed(
        access_zone_id=access_zone_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    access_zone_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[BadRequestResult, NotFoundResult, OkResult]]:
    """Check if the user is present in the access zone.

    Args:
        access_zone_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequestResult, NotFoundResult, OkResult]]
    """

    kwargs = _get_kwargs(
        access_zone_id=access_zone_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    access_zone_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[BadRequestResult, NotFoundResult, OkResult]]:
    """Check if the user is present in the access zone.

    Args:
        access_zone_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequestResult, NotFoundResult, OkResult]
    """

    return (
        await asyncio_detailed(
            access_zone_id=access_zone_id,
            client=client,
        )
    ).parsed
