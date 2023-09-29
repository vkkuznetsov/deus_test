from abc import ABC, abstractmethod
from typing import Dict, Optional, TypeVar, Union

from pydeus.types.responses.base import BaseResponse

ResponseModel = TypeVar('ResponseModel', bound=BaseResponse)


class ABCHTTPClient(ABC):
    """Represents an abstract HTTP client."""

    @abstractmethod
    def __init__(self) -> None:
        """Initialize an abstract HTTP client."""

    @abstractmethod
    async def request(
        self,
        endpoint: str,
        method: str,
        response_model: Optional[ResponseModel] = None,
        query_params: Optional[Dict[str, str]] = None,
        payload: Optional[Dict[str, str]] = None,
    ) -> Union[BaseResponse, Dict[str, str]]:
        """Make request"""

    @property
    @abstractmethod
    def authorization_token(self) -> str:
        """Authorotization token for modeus"""

    @authorization_token.setter
    @abstractmethod
    def authorization_token(self, token: str) -> None:
        """Setter for authorization token"""
