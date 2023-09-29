from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pydeus.client.abc import ABCModusClient


class BaseAPICategory:
    """Represents an API category."""

    def __init__(self, client: 'ABCModusClient') -> None:
        """
        Initialize the API category.

        Args:
            client: ABCModeusClient
        """
        self.client = client
