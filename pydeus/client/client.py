from __future__ import annotations

import asyncio
from typing import Optional

import jwt

from pydeus.client import ABCModusClient
from pydeus.client.authentication import ABCAuthentication, ModeusAuthentication
from pydeus.http.api import ABCHTTPClient, ModeusAPIClient
from pydeus.types import Credentials


class ModeusClient(ABCModusClient):
    """Respresents a modeus client."""

    def __init__(
        self,
        credentials: Credentials,
        *,
        auto_relogin: bool = True,
        authentication: Optional[ABCAuthentication] = None,
        api_client: Optional[ABCHTTPClient] = None,
        loop: Optional[asyncio.AbstractEventLoop] = None,
    ) -> None:
        """
        Initialize the ModeusClient.

        Args:
            credentials: Credentials
            auto_relogin: bool
            authentication: Optional[ABCAuthentication]
            api_client: Optional[ModeusAPIClient]
            loop: Optional[asyncio.AbstractEventLoop]
        """
        self.authentication = authentication or ModeusAuthentication()
        self.api_client = api_client or ModeusAPIClient()
        self.auto_relogin = auto_relogin
        self.credentials = credentials
        self.loop = loop or asyncio.get_event_loop()

        if self.credentials.bearer:
            self.person_id = self._get_person_id_from_bearer(self.credentials.bearer)

    async def auth(self, credentials: Optional[Credentials] = None) -> None:
        """Authentication api client to modeus

        Args:
            credentials: Optional[Credentials] - if parameter is None argument will take from self.credentials
        """
        credentials_ = credentials or self.credentials
        self.credentials = await self.authentication.login(credentials_)
        self.api_client.authorization_token = self.credentials.bearer
        self.person_id = self._get_person_id_from_bearer(self.credentials.bearer)

    def _get_person_id_from_bearer(self, bearer: str) -> str:
        return jwt.decode(
            bearer,
            algorithms=['RS256'],
            options={'verify_signature': False},
        ).get('person_id')
