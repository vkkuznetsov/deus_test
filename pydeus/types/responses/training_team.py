from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, Field, validator

from pydeus.types._validators import normalize_href_data
from pydeus.types.responses.base import BaseResponse


class TrainingTeamLinks(BaseModel):
    """Represents a training team links in json."""

    module: UUID = Field(..., alias='course-unit-realization')


class TrainingTeamResponseData(BaseModel):
    """Represents a training team response data in json."""

    type_name: str = Field(..., alias='name')
    name_short: str = Field(..., alias='nameShort')
    code: str
    module_short_name: str = Field(..., alias='courseUnitRealizationNameShort')
    links: TrainingTeamLinks = Field(..., alias='_links')
    id: UUID

    _normilize_href_data = validator('links', pre=True, allow_reuse=True)(
        normalize_href_data,
    )


class TrainingTeamResponse(BaseResponse):
    """Represents a training team JSON response."""

    teams: Optional[List[TrainingTeamResponseData]] = Field(None, alias='cycle-realizations')
