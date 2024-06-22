import unittest
from unittest.mock import patch, MagicMock
from api_session import RequestsAPISession, get_api_session


class TestRequestsAPISession(unittest.TestCase):

    def test_get_api_session_returns_instance(self):
        """Test get_api_session returns an instance of RequestsAPISession."""
        session = get_api_session()
        self.assertIsInstance(session, RequestsAPISession)

    def test_auth_session_sets_headers(self):
        """Test auth_session correctly sets headers."""
        session = RequestsAPISession()
        username = "user"
        key = "key123"
        session.auth_session(username, key)
        self.assertEqual(session.headers["NETOAPI_USERNAME"], username)
        self.assertEqual(session.headers["NETOAPI_KEY"], key)
        self.assertEqual(session.headers["Accept"], "application/json")

    @patch("api_session.requests.Session.post")
    def test_send_request_sends_post_request(self, mock_post):
        """Test send_request sends a POST request with the correct headers."""
        session = RequestsAPISession()
        session.headers = {"Existing": "Header"}
        
        mock_response = MagicMock()
        mock_post.return_value = mock_response
        
        url = "https://example.com/api"
        payload = {"data": "value"}
        headers = {"NETOAPI_ACTION": "testAction"}
        session.send_request(url=url, headers=headers, json=payload)
        
        # Assert post was called once
        mock_post.assert_called_once_with(url=url, headers=headers, json=payload)
        
        # Assert Existing header is not lost
        self.assertIn("Existing", session.headers)
        self.assertEqual(session.headers["Existing"], "Header")
        # Assert NETOAPI_ACTION header does not persist in session
        self.assertNotIn("NETOAPI_ACTION", session.headers)


if __name__ == "__main__":
    unittest.main()