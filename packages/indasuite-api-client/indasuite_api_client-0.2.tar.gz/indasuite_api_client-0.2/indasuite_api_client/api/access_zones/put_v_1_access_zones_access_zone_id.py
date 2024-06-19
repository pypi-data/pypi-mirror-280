from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.access_zone_update import AccessZoneUpdate
from ...models.error_response import ErrorResponse
from ...models.response_with_access_zone import ResponseWithAccessZone
from ...types import Response


def _get_kwargs(
    access_zone_id: str,
    *,
    body: Union[
        AccessZoneUpdate,
        AccessZoneUpdate,
        AccessZoneUpdate,
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/v1/access-zones/{access_zone_id}",
    }

    if isinstance(body, AccessZoneUpdate):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, AccessZoneUpdate):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "text/json"
    if isinstance(body, AccessZoneUpdate):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, ResponseWithAccessZone]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ResponseWithAccessZone.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, ResponseWithAccessZone]]:
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
    body: Union[
        AccessZoneUpdate,
        AccessZoneUpdate,
        AccessZoneUpdate,
    ],
) -> Response[Union[ErrorResponse, ResponseWithAccessZone]]:
    """Update access zone

     API custom return codes :
    1050 - Invalid request
    1305 - Name already exists
    1310 - Default access zone cannot be created/updated/deleted
    1400 - Unidentified error

    Args:
        access_zone_id (str):
        body (AccessZoneUpdate):
        body (AccessZoneUpdate):
        body (AccessZoneUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, ResponseWithAccessZone]]
    """

    kwargs = _get_kwargs(
        access_zone_id=access_zone_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    access_zone_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        AccessZoneUpdate,
        AccessZoneUpdate,
        AccessZoneUpdate,
    ],
) -> Optional[Union[ErrorResponse, ResponseWithAccessZone]]:
    """Update access zone

     API custom return codes :
    1050 - Invalid request
    1305 - Name already exists
    1310 - Default access zone cannot be created/updated/deleted
    1400 - Unidentified error

    Args:
        access_zone_id (str):
        body (AccessZoneUpdate):
        body (AccessZoneUpdate):
        body (AccessZoneUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, ResponseWithAccessZone]
    """

    return sync_detailed(
        access_zone_id=access_zone_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    access_zone_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        AccessZoneUpdate,
        AccessZoneUpdate,
        AccessZoneUpdate,
    ],
) -> Response[Union[ErrorResponse, ResponseWithAccessZone]]:
    """Update access zone

     API custom return codes :
    1050 - Invalid request
    1305 - Name already exists
    1310 - Default access zone cannot be created/updated/deleted
    1400 - Unidentified error

    Args:
        access_zone_id (str):
        body (AccessZoneUpdate):
        body (AccessZoneUpdate):
        body (AccessZoneUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, ResponseWithAccessZone]]
    """

    kwargs = _get_kwargs(
        access_zone_id=access_zone_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    access_zone_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        AccessZoneUpdate,
        AccessZoneUpdate,
        AccessZoneUpdate,
    ],
) -> Optional[Union[ErrorResponse, ResponseWithAccessZone]]:
    """Update access zone

     API custom return codes :
    1050 - Invalid request
    1305 - Name already exists
    1310 - Default access zone cannot be created/updated/deleted
    1400 - Unidentified error

    Args:
        access_zone_id (str):
        body (AccessZoneUpdate):
        body (AccessZoneUpdate):
        body (AccessZoneUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, ResponseWithAccessZone]
    """

    return (
        await asyncio_detailed(
            access_zone_id=access_zone_id,
            client=client,
            body=body,
        )
    ).parsed
