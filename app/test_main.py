from unittest import mock
from unittest.mock import MagicMock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(mocked_valid_google_url: MagicMock,
                                mocked_has_internet_connection: MagicMock
                                ) -> None:
    assert can_access_google_page("url") == "Accessible"
    mocked_has_internet_connection.assert_called_once()
    mocked_valid_google_url.assert_called_once()
