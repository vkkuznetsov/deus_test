from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, Field

from pydeus.types.responses.base import BaseResponse


class BuildingResponseData(BaseModel):
    """Represents buidling data in response."""

    name: str
    address: str
    id: UUID


class RoomResponseData(BaseModel):
    """Represents room data in response."""

    name: str = Field(..., alias='name')
    capacity: int = Field(0, alias='totalCapacity')
    project_availiable: bool = Field(default=False, alias='projectorAvailable')
    building: BuildingResponseData
    id: UUID


class RoomResponse(BaseResponse):
    """Represents a room JSON response."""

    rooms: Optional[List[RoomResponseData]] = None
