from __future__ import annotations
from netoapi.api_session import get_api_session
from netoapi.errors import NetoAPIRequestError


class NetoAPIClient:
    """The api client class provides a persistent HTTP session
    and the functionality to execute api requests"""

    def __init__(self, endpoint: str, username: str, key: str) -> None:
        self.endpoint = endpoint

        self._session = get_api_session()
        self._session.auth_session(username, key)

        self._connection_timeout = 5
        self._response_timeout = 5

    @property
    def timeout(self) -> tuple:
        """Sets the values in seconds for connection & request timeouts
        respectively. Set each value with a tuple(int, int) or set both to
        the same value with an integer. Set either or both to None if you
        want to disable that timeout and wait forever."""
        return (self._connection_timeout, self._response_timeout)

    @timeout.setter
    def timeout(self, val: int | None | tuple[int | None, int | None]):
        if not val or type(val) == int:
            self._connection_timeout = val
            self._response_timeout = val
        elif type(val) == tuple:
            self._connection_timeout = val[0]
            self._response_timeout = val[1]
        else:
            raise TypeError(
                f"timeout value must be int or tuple(int,int) or None not {type(val).__name__}"
            )

    def execute_api_call(self, action: str, payload: dict) -> dict:
        """Execute an api call and return the JSON response"""

        try:
            response = self._session.send_request(
                url=self.endpoint,
                headers={"NETOAPI_ACTION": action},
                json=payload,
                timeout=(self.timeout),
            )
            response.raise_for_status()
            api_response: dict = response.json()

        except Exception as e:
            raise NetoAPIRequestError(
                f"An error occured during the request: {e}"
            ) from None

        return api_response
