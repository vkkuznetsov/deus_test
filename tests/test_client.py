import pytest

from pydeus.client.authentication import ModeusAuthentication
from pydeus.types.credentials import Credentials


@pytest.mark.with_env
async def test_auth(env_credentials: Credentials):
    modeus_auth = ModeusAuthentication()
    credentials = await modeus_auth.login(env_credentials)
    assert credentials.bearer is not None
    assert credentials.email is not None
    assert credentials.password is not None
