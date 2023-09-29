from typing import List, Optional

from pydantic import BaseModel

from pydeus.types.responses.base import BaseResponse


class SpecialtiesResponseData(BaseModel):
    """Represents specialties data in json response."""

    name: str
    code: str
    id: str


class SpecialtiesResponse(BaseResponse):
    """Represents a specialties json response."""

    specialties: Optional[List[SpecialtiesResponseData]] = None
