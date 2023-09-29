from typing import List, Optional, Union
from uuid import UUID

from pydantic import BaseModel, Field, validator

from pydeus.types._validators import normalize_href_data
from pydeus.types.responses.base import BaseResponse


class ModuleLinks(BaseModel):
    planning_period: Union[UUID, str] = Field(..., alias='planning-period')


class ModuleResponseData(BaseModel):
    """Represents module data in json response."""

    name: Optional[str] = None
    name_short: str = Field(None, alias='nameShort')
    prototype_id: UUID = Field(..., alias='prototypeId')
    links: ModuleLinks = Field(..., alias='_links')
    id: UUID

    # validators
    _normilize_href_data = validator('links', pre=True, allow_reuse=True)(
        normalize_href_data,
    )


class PlaningPeriodData(BaseModel):
    """Represents planing period data in json response."""

    name: Optional[str] = None
    id: UUID


class ModuleResponse(BaseResponse):
    """Represents a module json response."""

    modules: Optional[List[ModuleResponseData]] = Field(
        None,
        alias='course-unit-realizations',
    )
    planning_periods: Optional[List[PlaningPeriodData]] = Field(
        None,
        alias='planning-periods',
    )
