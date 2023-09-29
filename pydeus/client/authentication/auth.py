import re
import secrets
from typing import Dict, Optional

import httpx
from bs4 import BeautifulSoup

import pydeus
from pydeus.client.authentication.abc import ABCAuthentication
from pydeus.types import Credentials
from pydeus.types.app_config import AppConfigJSON
from pydeus.types.requests.authentication import (
    AdfsAuthenticationBodyRequest,
    OAuth2QueryRequest,
)
from pydeus.types.urls import ModeusURL

TOKEN_LENGTH = 16


class ModeusAuthentication(ABCAuthentication):
    """Default modeus authentication."""

    def __init__(self):
        """Initialize the default Modeus authentication."""
        self._session = httpx.AsyncClient(
            headers={'User-Agent': pydeus.user_agent_header},
            follow_redirects=True,
        )

    async def login(self, credentials: Credentials) -> Credentials:
        """
        Login in Modeus.

        Args:
            credentials: Credentials

        Returns:
            Credentials
        """
        oauth2_response = await self._oauth2_request()
        adfs_response: Dict[str, str] = await self._get_adfs_response(
            oauth2_response.url,
            credentials,
        )
        token = await self._get_bearer_token(adfs_response)

        return Credentials(
            email=credentials.email,
            password=credentials.password,
            bearer=token,
        )

    async def _oauth2_request(self) -> httpx.Response:
        """
        Start authentication process.

        Returns:
            httpx.Response
        """
        app_config: AppConfigJSON = await self._get_app_config_json()

        request_query = OAuth2QueryRequest(
            client_id=app_config.wso.client_id,
            redirect_uri=app_config.wso.redirect_url,
            state=secrets.token_hex(TOKEN_LENGTH),
            nonce=secrets.token_hex(TOKEN_LENGTH),
        ).dict()

        return await self._session.get(ModeusURL.oauth2, params=request_query)

    async def _get_app_config_json(self) -> AppConfigJSON:
        """
        Return app.config.json from Modeus.

        Returns:
            AppConfigJSON
        """
        response = await self._session.get(ModeusURL.app_config_json)
        return AppConfigJSON(**response.json())

    async def _get_adfs_response(
        self,
        oauth2_response_url: str,
        credentials: Credentials,
    ) -> Dict[str, str]:
        """
        Return adfs response from url from self._oauth2_request.

        Args:
            oauth2_response_url: str
            credentials: Credentials

        Returns:
            Dict[str, str]
        """
        adfs_form_data = AdfsAuthenticationBodyRequest(
            UserName=credentials.email,
            Password=credentials.password,
        ).dict(by_alias=True)

        response = await self._session.post(
            oauth2_response_url,
            data=adfs_form_data,
        )

        html = BeautifulSoup(response.text, 'html.parser')
        auth_data = {}

        for el in html.form.find_all('input', type='hidden'):
            auth_data[el['name']] = el['value']

        return auth_data

    async def _get_bearer_token(self, adfs_response: Dict[str, str]) -> Optional[str]:
        """
        Return bearer token if it exists, otherwise return None.

        Args:
            adfs_response: Dict[str, str] - response from self._get_adfs_response

        Returns:
            Optional[str]
        """
        response = await self._session.post(
            ModeusURL.commonauth,
            data=adfs_response,
        )

        token_raw = response.url.fragment
        re_pattern = 'id_token=(.*)&state'
        token: Optional[str]

        try:
            token: str = re.findall(re_pattern, token_raw)[0]
        except IndexError:
            token = None
        finally:
            await self._session.aclose()

        return token
