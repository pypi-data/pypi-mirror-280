"""Contains shared errors types that can be raised from API functions"""

import logging
from httpx import codes
from .models import ErrorResponse, WarningResponse


class UnexpectedStatus(Exception):
    """Raised by api functions when the response status an undocumented status and Client.raise_on_unexpected_status is True"""

    def __init__(self, status_code: int, content: bytes):
        self.status_code = status_code
        self.content = content

        super().__init__(
            f"Unexpected status code - {status_code}\n{content.decode(errors='ignore')}"
        )


def unexpected_status_handler(func):
    """
    A decorator that handles UnexpectedStatus raised by a function and transform http ErrorResponse to an UnexpectedStatus Exception.
    This decorator should be used in every interface methods of SDK.
    """

    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            if isinstance(result, (ErrorResponse, WarningResponse)):
                status_code = result.status_code
                message = ""

                if isinstance(result.message, str):
                    message = result.message

                if isinstance(result.errors, list):
                    for error in result.errors:
                        message += f"\n\t{error.error} - {error.message}"

                raise UnexpectedStatus(status_code, message.encode())

            return result
        except UnexpectedStatus as error:
            phrase = codes.get_reason_phrase(error.status_code)
            logging.error(
                f"An error occurred: {error} \nStatus code {error.status_code} - {phrase if phrase else 'Internal status code'}\n"
            )

    return wrapper


__all__ = ["UnexpectedStatus", "unexpected_status_handler"]
