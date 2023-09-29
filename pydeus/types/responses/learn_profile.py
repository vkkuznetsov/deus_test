from typing import List, Optional, Union
from uuid import UUID

from pydantic import BaseModel, Field

from pydeus.types.responses.base import BaseResponse


class LearningProfileResponseData(BaseModel):
    """Represents a learning profile response data in json"""

    name: str
    specialties_code: str = Field(..., alias='specialtyId')
    id: Union[UUID, str]


class LearnProfileResponse(BaseResponse):
    """Represents a learning profile json response."""

    profiles: Optional[List[LearningProfileResponseData]] = None
