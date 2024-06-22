import unittest
from unittest.mock import patch, MagicMock
from requests import Response
from requests.exceptions import HTTPError
from api_client import NetoAPIClient
from api_session import RequestsAPISession
from errors import NetoAPIRequestError


class TestNetoAPIClient(unittest.TestCase):
    
    def setUp(self):
        """Set up a generic NetoAPIClient instance for testing."""
        self.client = NetoAPIClient(endpoint="https://example.com/api", username="user", key="key123")

    @patch("api_client.get_api_session")
    def test_init_auth_session_called(self, mock_get_api_session):
        """Test that auth_session is correctly called on initialization."""
        mock_session = mock_get_api_session.return_value
        NetoAPIClient("https://example.com/api", "user", "key123")
        mock_session.auth_session.assert_called_once_with("user", "key123")

    def test_timeout_property(self):
        """Test setting and getting timeout property."""
        self.client.timeout = 10
        self.assertEqual(self.client.timeout, (10, 10))
        
        self.client.timeout = (5, 15)
        self.assertEqual(self.client.timeout, (5, 15))

        with self.assertRaises(TypeError):
            self.client.timeout = "invalid"


    @patch("requests.Session.post")
    def test_execute_api_call(self, mock_post):
        """Test executing an API call."""
        mock_response = MagicMock(spec=Response)
        mock_response.status_code = 200
        mock_response.json.return_value = {"success": True}
        
        mock_post.return_value = mock_response
        
        action = "testAction"
        payload = {"data": "value"}

        response = self.client.execute_api_call(action, payload)
        
        self.assertEqual(response, {"success": True})
        mock_post.assert_called_once()

    # @patch("requests.Session.post")
    # def test_execute_api_call_with_error(self, mock_post):
    #     """Test executing an API call that raises an exception."""
    #     mock_post.side_effect = HTTPError("Test Error")
        
    #     action = "testAction"
    #     payload = {"data": "value"}
        
    #     with self.assertRaises(NetoAPIRequestError):
    #         self.client.execute_api_call(action, payload)
            


if __name__ == "__main__":
    unittest.main()