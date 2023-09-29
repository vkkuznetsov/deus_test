from typing import Any

import pytest

from pydeus.client import ModeusClient
from pydeus.types import Credentials
from tests._test_utils import MockedAPIClient


@pytest.fixture
async def authorized_client(env_credentials) -> ModeusClient:
    client = ModeusClient(env_credentials)
    await client.auth()
    assert client.credentials.bearer is not None
    return client


@pytest.fixture
def mocked_api_client() -> ModeusClient:
    def get_api_client(return_value: Any) -> ModeusClient:
        client = ModeusClient(
            credentials=Credentials(
                email='altdeus@staypony.space', password='https://altdeus.staypony.space/'
            )
        )
        client.api_client = MockedAPIClient(return_value)
        return client

    return get_api_client
