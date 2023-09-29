import os

import pytest

from pydeus.types.credentials import Credentials


@pytest.fixture
def env_credentials() -> Credentials:
    return Credentials(
        email=os.getenv('EMAIL'),
        password=os.getenv('PASSWORD'),
    )
