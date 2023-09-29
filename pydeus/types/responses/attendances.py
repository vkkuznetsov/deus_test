from __future__ import annotations

from enum import Enum
from typing import Optional
from uuid import UUID

from pydantic import Field

from pydeus.types.responses.base import BaseResponse


class EventTeamResponse(BaseResponse):
    first_name: str = Field(..., alias='firstName')
    last_name: str = Field(..., alias='lastName')
    middle_name: Optional[str] = Field(None, alias='middleName')
    full_name: str = Field(..., alias='fullName')
    role_id: RolesType = Field(..., alias='roleId')
    id: UUID
    person_id: UUID = Field(..., alias='personId')


class RolesType(Enum):
    STUDENT = 'STUDENT'
    TEACHER = 'TEACH'


EventTeamResponse.update_forward_refs()
