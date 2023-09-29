from pydantic import Field, validator

from pydeus.types._validators import normalize_href_data
from pydeus.types.responses.base import BaseResponse


class LessonRealizationDataResponse(BaseResponse):
    """Represents a lesson realization data in json response."""

    name: str
    name_short: str = Field(..., alias='nameShort')
    code: str
    links: dict
    id: str

    _normilize_href_data = validator('links', pre=False, allow_reuse=True)(
        normalize_href_data,
    )
