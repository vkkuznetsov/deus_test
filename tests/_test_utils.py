from typing import Any, Dict, Optional, Union

from pydantic import BaseModel

from pydeus.http.abc import ABCHTTPClient, ResponseModel
from pydeus.types.responses.base import BaseResponse


class MockedAPIClient(ABCHTTPClient):
    def __init__(self, return_value: Optional[Any]) -> None:
        self.return_value = return_value

    async def request(
        self,
        endpoint: str,  # noqa
        method: str,  # noqa
        response_model: Optional[ResponseModel] = None,  # noqa
        query_params: Optional[Dict[str, str]] = None,  # noqa
        payload: Optional[Dict[str, str]] = None,  # noqa
    ) -> Union[BaseResponse, Dict[str, str]]:
        return response_model.parse_obj(self.return_value)

    @property
    def authorization_token(self) -> str:
        pass

    @authorization_token.setter
    def authorization_token(self, token: str) -> None:
        pass


def check_model_values_is_not_none(model: BaseModel, exclude: Optional[set] = None):
    for value in model.dict(exclude=exclude).values():
        assert value is not None
