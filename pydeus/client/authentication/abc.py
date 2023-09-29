from abc import ABC, abstractmethod

from pydeus.types import Credentials


class ABCAuthentication(ABC):
    """Abstract modeus authentication"""

    @abstractmethod
    def __init__(self):
        """Initialize the authentication."""
        raise NotImplementedError

    @abstractmethod
    async def login(self, credentials: Credentials) -> Credentials:
        """Login in modeus via the given email and password."""
        raise NotImplementedError
