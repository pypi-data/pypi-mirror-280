from typing import Tuple
import logging

from ..client import RefreshTokenClient
from .models import RefreshTokenRequest, TokenResponse, Error, Message
from .api import post_refresh


def refresh_access_token(
    device_auth_base_url: str, api_key: str, client_id: str, refresh_token: str
) -> Tuple[str, str]:
    """
    Get new device access token.

    Args:
        device_auth_base_url (str): The base URL for the authentication API, token refresh request is done to this URL.
        client_id (str): The client id to use for authentication.
        refresh_token (str): The refresh token to use.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.
        Exception: if server was unable to refresh token.

    Returns:
        access_token and refresh_token as Tuple(str, str)
    """
    refresh_token_client = RefreshTokenClient(
        base_url=device_auth_base_url, api_key=api_key
    )
    request: RefreshTokenRequest = RefreshTokenRequest.from_dict(
        {"refresh_token": refresh_token, "client_id": client_id}
    )
    with refresh_token_client as refresh_token_client:
        response = post_refresh.sync(client=refresh_token_client, body=request)
        logging.debug(f"{response}")

        if isinstance(response, TokenResponse):
            logging.debug(f"{response.access_token=}")
            access_token = response.access_token

            logging.debug(f"{response.refresh_token =}")
            refresh_token = response.refresh_token

            return access_token, refresh_token

        elif isinstance(response, Error | Message):
            raise Exception(response.to_dict())

        else:
            raise Exception("Unexpected error occured refreshing token")
