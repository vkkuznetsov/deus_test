from typing import Dict, List, Optional, Union

import httpx
from pydantic import parse_obj_as

import pydeus
from pydeus.errors.http.errors import MethodNotFoundError
from pydeus.http.abc import ABCHTTPClient, ResponseModel
from pydeus.types.responses.base import BaseResponse


class ModeusAPIClient(ABCHTTPClient):
    """Represents HTTP client."""

    def __init__(self) -> None:
        """Initialize HTTP client."""
        self._session = httpx.AsyncClient(
            headers={
                'User-Agent': pydeus.user_agent_header,
                'Content-Type': 'application/json',
            },
        )
        self._authorization_token: str = None

    @property
    def authorization_token(self) -> str:
        return self._authorization_token

    @authorization_token.setter
    def authorization_token(self, token: str) -> None:
        self._session.headers.update({'Authorization': 'Bearer {}'.format(token)})
        self._authorization_token = token

    async def request(
        self,
        endpoint: str,
        method: str,
        response_model: Optional[ResponseModel] = None,
        query_params: Optional[Dict[str, str]] = None,
        payload: Optional[Dict[str, str]] = None,
    ) -> Union[BaseResponse, Dict[str, str]]:
        """
        Make request.

        Args:
            endpoint: str
            method: str
            response_model: str
            query_params: Optional[Dict[str, str]]
            payload: Optional[Dict[str, str]]

        Returns:
            Union[BaseResponse, Dict[str, str]]
            BaseResponse: if you pass it as argument, otherwise return raw dict

        Raises:
            MethodNotFoundError: when method is not defined
        """
        response: Optional[httpx.Response]

        if method.lower() == 'get':
            response = await self._get(endpoint, query_params)
        elif method.lower() == 'post':
            response = await self._post(
                endpoint,
                query_params,
                payload,
            )
        else:
            raise MethodNotFoundError(
                'Method "{0}" not found. Did you implement it?'.format(method),
            )

        # TODO: Добавить обработку ошибок от модеуса

        if response_model:
            response_json = response.json()
            return self._parse_obj(response_model, response_json)
        return response.json()

    async def _post(
        self,
        endpoint: str,
        query_params: Optional[Dict[str, str]] = None,
        payload: Optional[Dict[str, str]] = None,
    ) -> httpx.Response:
        """
        Post HTTP request.

        Args:
            endpoint: str
            query_params: Optional[Dict[str, str]]
            payload: Optional[Dict[str, str]]

        Returns:
            httpx.Response
        """
        return await self._session.post(endpoint, params=query_params, data=payload)

    async def _get(
        self,
        endpoint: str,
        query_params: Optional[Dict[str, str]] = None,
    ) -> httpx.Response:
        """
        Get HTTP request.

        Args:
            endpoint: str
            query_params: Optional[Dict[str, str]]

        Returns:
            httpx.Response
        """
        return await self._session.get(endpoint, params=query_params)

    def _parse_obj(
        self, response_model: ResponseModel, response_json: Dict
    ) -> Union[ResponseModel, List[ResponseModel]]:
        if isinstance(response_json, dict):
            return response_model.parse_obj(response_json)
        elif isinstance(response_json, list):
            return parse_obj_as(List[response_model], response_json)
        else:
            raise TypeError('Not supported response_json type')
