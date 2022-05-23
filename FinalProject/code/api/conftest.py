import pytest

from api.client.api_client import ApiClient
from userdata import creds


@pytest.fixture(scope="function")
def api_client() -> ApiClient:
    api_client = ApiClient(user=creds.login, password=creds.password)
    api_client.post_login(creds.login, creds.password)
    return api_client
