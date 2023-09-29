import asyncio
from abc import ABC, abstractmethod
from typing import Optional

from pydeus.api.search_category import SearchAPICaterogry
from pydeus.api.timetable_category import TimetableAPICategory
from pydeus.client.authentication import ABCAuthentication
from pydeus.http.api import ABCHTTPClient
from pydeus.types import Credentials


class ABCModusClient(ABC):
    """Abstract modeus client."""

    credentials: Credentials
    auto_relogin: bool
    authentication: Optional[ABCAuthentication]
    api_client: Optional[ABCHTTPClient]
    loop: Optional[asyncio.AbstractEventLoop]

    @abstractmethod
    def __init__(self) -> None:
        """Initialize the client."""
        raise NotImplementedError

    @property
    def timetable(self) -> TimetableAPICategory:
        return TimetableAPICategory(self)

    @property
    def search(self) -> SearchAPICaterogry:
        return SearchAPICaterogry(self)
