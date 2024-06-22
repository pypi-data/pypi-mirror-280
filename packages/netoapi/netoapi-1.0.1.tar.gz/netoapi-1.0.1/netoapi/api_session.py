"""Provides transport pathways for API requests"""

from abc import ABC, abstractmethod

import requests


class NetoAPISession(ABC):
    """Abstract interface for API transport sessions"""

    @abstractmethod
    def auth_session():
        """Sets the authentication headers to be sent with API requests.
        These headers persist between requests."""

    @abstractmethod
    def send_request():
        """Fetches data from the API. The 'NETOAPI_ACTION' header is
        appended to the session headers but does not persist
        between requests."""


class RequestsAPISession(NetoAPISession, requests.Session):
    """An HTTP session which sub-classes requests.Session"""

    def __init__(self) -> None:
        super().__init__()

    def auth_session(self, username: str, key: str) -> None:
        """Sets the authentication headers to be sent with API requests.
        These headers persist between requests."""
        self.headers = {
            "NETOAPI_USERNAME": username,
            "NETOAPI_KEY": key,
            "Accept": "application/json",
        }

    def send_request(self, **kwargs) -> requests.Response:
        """Sends the HTTP post request to the API. The 'NETOAPI_ACTION'
        header is appended to the session headers but does not persist
        between requests."""
        return self.post(**kwargs)


def get_api_session():
    """Returns a session object. This is the correct way to get a session,
    rather than creating instances directly."""
    return RequestsAPISession()
