import logging
from attrs import define

from deprecated import deprecated
from .http_client import TokenClient, AuthenticatedClient

from ..auth import get_token, ResponseWithToken


@deprecated("Use AuthenticatedClient instead with your access token.")
@define
class APIClient:
    """A Client which get authentication token with secret/id and then use it on secured endpoints

    Attributes:
        api_url: The base URL for the API, all requests are made to a relative path to this URL.
        token_url: The base URL for the authentication API, token request is done to this URL.
        client_id: The client id to use for authentication.
        client_secret: The client secret to use for authentication.
        audience: The URL of the intended consumer of the token. In other words, the URL of the resource server that a client would like to access.

    The following are accepted as keyword arguments and will be used to get token:
        ``grant_type``: grant_type attribute in token request body. Default value is 'client_credentials'.

    """
    def __new__(cls, 
                api_url,
                token_url,
                client_id,
                client_secret,
                audience,
                grant_type = "client_credentials"):

        token_client = TokenClient(
            client_id=client_id,
            client_secret=client_secret,
            base_url=token_url,
            audience=audience,
            grant_type=grant_type
            )
        with token_client as token_client:
            response: ResponseWithToken = get_token.sync(client=token_client)
            logging.debug(f"{response.access_token=}")
            access_token = response.access_token

        if not access_token:
            raise Exception("Unable to get token with provided information.")

        auth_client = AuthenticatedClient(
            base_url=api_url,
            token=access_token,
            raise_on_unexpected_status=True)

        return auth_client
