from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.ok_response import OkResponse
from ...models.post_v1_databases_datasource_import_body import PostV1DatabasesDatasourceImportBody
from ...models.warning_response import WarningResponse
from ...types import Response


def _get_kwargs(
    datasource: str,
    *,
    body: PostV1DatabasesDatasourceImportBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/v1/databases/{datasource}/import",
    }

    _body = body.to_multipart()

    _kwargs["files"] = _body

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, OkResponse, WarningResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = OkResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.ACCEPTED:
        response_202 = WarningResponse.from_dict(response.json())

        return response_202
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, OkResponse, WarningResponse]]:
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
    body: PostV1DatabasesDatasourceImportBody,
) -> Response[Union[ErrorResponse, OkResponse, WarningResponse]]:
    """Ingest Excel/Csv values. Automatically creates non existent time series. Beware: only send points if
    you are absolutely certain they should be persisted.

     API custom return codes :
    1020 - Error from database engine
    1021 - Invalid datasource name
    1022 - Out of range timestamp
    1050 - Invalid request
    1500 - Internal server error
    1501 - Warning

    Args:
        datasource (str):
        body (PostV1DatabasesDatasourceImportBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, OkResponse, WarningResponse]]
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
    body: PostV1DatabasesDatasourceImportBody,
) -> Optional[Union[ErrorResponse, OkResponse, WarningResponse]]:
    """Ingest Excel/Csv values. Automatically creates non existent time series. Beware: only send points if
    you are absolutely certain they should be persisted.

     API custom return codes :
    1020 - Error from database engine
    1021 - Invalid datasource name
    1022 - Out of range timestamp
    1050 - Invalid request
    1500 - Internal server error
    1501 - Warning

    Args:
        datasource (str):
        body (PostV1DatabasesDatasourceImportBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, OkResponse, WarningResponse]
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
    body: PostV1DatabasesDatasourceImportBody,
) -> Response[Union[ErrorResponse, OkResponse, WarningResponse]]:
    """Ingest Excel/Csv values. Automatically creates non existent time series. Beware: only send points if
    you are absolutely certain they should be persisted.

     API custom return codes :
    1020 - Error from database engine
    1021 - Invalid datasource name
    1022 - Out of range timestamp
    1050 - Invalid request
    1500 - Internal server error
    1501 - Warning

    Args:
        datasource (str):
        body (PostV1DatabasesDatasourceImportBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, OkResponse, WarningResponse]]
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
    body: PostV1DatabasesDatasourceImportBody,
) -> Optional[Union[ErrorResponse, OkResponse, WarningResponse]]:
    """Ingest Excel/Csv values. Automatically creates non existent time series. Beware: only send points if
    you are absolutely certain they should be persisted.

     API custom return codes :
    1020 - Error from database engine
    1021 - Invalid datasource name
    1022 - Out of range timestamp
    1050 - Invalid request
    1500 - Internal server error
    1501 - Warning

    Args:
        datasource (str):
        body (PostV1DatabasesDatasourceImportBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, OkResponse, WarningResponse]
    """

    return (
        await asyncio_detailed(
            datasource=datasource,
            client=client,
            body=body,
        )
    ).parsed
