from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.access_type import AccessType
from ...models.response_with_access_zone_list import ResponseWithAccessZoneList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    only_default: Union[Unset, AccessType] = UNSET,
    include_groups: Union[Unset, bool] = True,
    name: Union[Unset, str] = UNSET,
    pagination_key: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 50,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_only_default: Union[Unset, str] = UNSET
    if not isinstance(only_default, Unset):
        json_only_default = only_default.value

    params["onlyDefault"] = json_only_default

    params["includeGroups"] = include_groups

    params["name"] = name

    params["paginationKey"] = pagination_key

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v1/access-zones",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ResponseWithAccessZoneList]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ResponseWithAccessZoneList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ResponseWithAccessZoneList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    only_default: Union[Unset, AccessType] = UNSET,
    include_groups: Union[Unset, bool] = True,
    name: Union[Unset, str] = UNSET,
    pagination_key: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 50,
) -> Response[ResponseWithAccessZoneList]:
    """Get all data access zones

    Args:
        only_default (Union[Unset, AccessType]):
        include_groups (Union[Unset, bool]):  Default: True.
        name (Union[Unset, str]):
        pagination_key (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResponseWithAccessZoneList]
    """

    kwargs = _get_kwargs(
        only_default=only_default,
        include_groups=include_groups,
        name=name,
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
    only_default: Union[Unset, AccessType] = UNSET,
    include_groups: Union[Unset, bool] = True,
    name: Union[Unset, str] = UNSET,
    pagination_key: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 50,
) -> Optional[ResponseWithAccessZoneList]:
    """Get all data access zones

    Args:
        only_default (Union[Unset, AccessType]):
        include_groups (Union[Unset, bool]):  Default: True.
        name (Union[Unset, str]):
        pagination_key (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResponseWithAccessZoneList
    """

    return sync_detailed(
        client=client,
        only_default=only_default,
        include_groups=include_groups,
        name=name,
        pagination_key=pagination_key,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    only_default: Union[Unset, AccessType] = UNSET,
    include_groups: Union[Unset, bool] = True,
    name: Union[Unset, str] = UNSET,
    pagination_key: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 50,
) -> Response[ResponseWithAccessZoneList]:
    """Get all data access zones

    Args:
        only_default (Union[Unset, AccessType]):
        include_groups (Union[Unset, bool]):  Default: True.
        name (Union[Unset, str]):
        pagination_key (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResponseWithAccessZoneList]
    """

    kwargs = _get_kwargs(
        only_default=only_default,
        include_groups=include_groups,
        name=name,
        pagination_key=pagination_key,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    only_default: Union[Unset, AccessType] = UNSET,
    include_groups: Union[Unset, bool] = True,
    name: Union[Unset, str] = UNSET,
    pagination_key: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 50,
) -> Optional[ResponseWithAccessZoneList]:
    """Get all data access zones

    Args:
        only_default (Union[Unset, AccessType]):
        include_groups (Union[Unset, bool]):  Default: True.
        name (Union[Unset, str]):
        pagination_key (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResponseWithAccessZoneList
    """

    return (
        await asyncio_detailed(
            client=client,
            only_default=only_default,
            include_groups=include_groups,
            name=name,
            pagination_key=pagination_key,
            limit=limit,
        )
    ).parsed
