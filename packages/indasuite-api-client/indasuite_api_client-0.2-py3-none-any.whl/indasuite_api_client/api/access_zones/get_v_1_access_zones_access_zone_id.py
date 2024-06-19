from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.response_with_access_zone import ResponseWithAccessZone
from ...types import UNSET, Response, Unset


def _get_kwargs(
    access_zone_id: str,
    *,
    include_groups: Union[Unset, bool] = True,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["includeGroups"] = include_groups

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/v1/access-zones/{access_zone_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ResponseWithAccessZone]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ResponseWithAccessZone.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ResponseWithAccessZone]:
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
    include_groups: Union[Unset, bool] = True,
) -> Response[ResponseWithAccessZone]:
    """Get Access Zone with id

     API custom return codes :
    1050 - Invalid request

    Args:
        access_zone_id (str):
        include_groups (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResponseWithAccessZone]
    """

    kwargs = _get_kwargs(
        access_zone_id=access_zone_id,
        include_groups=include_groups,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    access_zone_id: str,
    *,
    client: AuthenticatedClient,
    include_groups: Union[Unset, bool] = True,
) -> Optional[ResponseWithAccessZone]:
    """Get Access Zone with id

     API custom return codes :
    1050 - Invalid request

    Args:
        access_zone_id (str):
        include_groups (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResponseWithAccessZone
    """

    return sync_detailed(
        access_zone_id=access_zone_id,
        client=client,
        include_groups=include_groups,
    ).parsed


async def asyncio_detailed(
    access_zone_id: str,
    *,
    client: AuthenticatedClient,
    include_groups: Union[Unset, bool] = True,
) -> Response[ResponseWithAccessZone]:
    """Get Access Zone with id

     API custom return codes :
    1050 - Invalid request

    Args:
        access_zone_id (str):
        include_groups (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResponseWithAccessZone]
    """

    kwargs = _get_kwargs(
        access_zone_id=access_zone_id,
        include_groups=include_groups,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    access_zone_id: str,
    *,
    client: AuthenticatedClient,
    include_groups: Union[Unset, bool] = True,
) -> Optional[ResponseWithAccessZone]:
    """Get Access Zone with id

     API custom return codes :
    1050 - Invalid request

    Args:
        access_zone_id (str):
        include_groups (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResponseWithAccessZone
    """

    return (
        await asyncio_detailed(
            access_zone_id=access_zone_id,
            client=client,
            include_groups=include_groups,
        )
    ).parsed
