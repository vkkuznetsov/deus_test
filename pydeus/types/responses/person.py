from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, Field

from pydeus.types.responses.base import BaseResponse


class PersonResponseData(BaseModel):
    """Represents a person data in response."""

    first_name: str = Field(..., alias='firstName')
    last_name: str = Field(..., alias='lastName')
    middle_name: Optional[str] = Field(None, alias='middleName')
    full_name: str = Field(..., alias='fullName')
    id: UUID


class PersonResponse(BaseResponse):
    """Represents a persons JSON response."""

    persons: Optional[List[PersonResponseData]] = None
