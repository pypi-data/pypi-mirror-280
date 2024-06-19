from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.annotation_upsert import AnnotationUpsert
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    datasource: str,
    id: str,
    *,
    body: Union[
        AnnotationUpsert,
        AnnotationUpsert,
        AnnotationUpsert,
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/v1/databases/{datasource}/annotations/{id}",
    }

    if isinstance(body, AnnotationUpsert):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, AnnotationUpsert):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "text/json"
    if isinstance(body, AnnotationUpsert):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ErrorResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = cast(Any, None)
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
) -> Response[Union[Any, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    datasource: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        AnnotationUpsert,
        AnnotationUpsert,
        AnnotationUpsert,
    ],
) -> Response[Union[Any, ErrorResponse]]:
    """Update existing annotations

     API custom return codes :
    1050 - Invalid request
    1501 - Warning

    Args:
        datasource (str):
        id (str):
        body (AnnotationUpsert):
        body (AnnotationUpsert):
        body (AnnotationUpsert):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        datasource=datasource,
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    datasource: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        AnnotationUpsert,
        AnnotationUpsert,
        AnnotationUpsert,
    ],
) -> Optional[Union[Any, ErrorResponse]]:
    """Update existing annotations

     API custom return codes :
    1050 - Invalid request
    1501 - Warning

    Args:
        datasource (str):
        id (str):
        body (AnnotationUpsert):
        body (AnnotationUpsert):
        body (AnnotationUpsert):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse]
    """

    return sync_detailed(
        datasource=datasource,
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    datasource: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        AnnotationUpsert,
        AnnotationUpsert,
        AnnotationUpsert,
    ],
) -> Response[Union[Any, ErrorResponse]]:
    """Update existing annotations

     API custom return codes :
    1050 - Invalid request
    1501 - Warning

    Args:
        datasource (str):
        id (str):
        body (AnnotationUpsert):
        body (AnnotationUpsert):
        body (AnnotationUpsert):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        datasource=datasource,
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    datasource: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        AnnotationUpsert,
        AnnotationUpsert,
        AnnotationUpsert,
    ],
) -> Optional[Union[Any, ErrorResponse]]:
    """Update existing annotations

     API custom return codes :
    1050 - Invalid request
    1501 - Warning

    Args:
        datasource (str):
        id (str):
        body (AnnotationUpsert):
        body (AnnotationUpsert):
        body (AnnotationUpsert):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            datasource=datasource,
            id=id,
            client=client,
            body=body,
        )
    ).parsed
