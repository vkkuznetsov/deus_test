from typing import Union
from uuid import UUID

from pydantic import BaseModel


class Base(BaseModel):  # TODO: Название Base как то не очень. Base чего?
    """Represents a base of models."""

    id: Union[UUID, str]
