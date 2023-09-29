from datetime import datetime
from typing import List, Union
from uuid import UUID

from pydantic import Field, validator

from pydeus.types._validators import value_must_be_in_list
from pydeus.types.event import EventType
from pydeus.types.requests.base_request import BaseRequest

UUIDListOrStrOrNone = Union[List[UUID], List[str], str, UUID, None]


def python_datetime_to_java(value: datetime) -> str:
    """Convert a python datetime to a Java datetime.

    Args:
        value: datetime - python datetime object

    Returns:
        str - java datetime
    """
    return str(value.strftime('%Y-%m-%dT%H:%M:%SZ'))


class EventRequestJson(BaseRequest):
    """Represents a json for event request."""

    person_ids: UUIDListOrStrOrNone = Field(None, alias='attendeePersonId')
    learning_teams: UUIDListOrStrOrNone = Field(None, alias='cycleRealizationId')
    years_start_learning: Union[List[int], int, None] = Field(None, alias='learningStartYear')
    learning_profiles: UUIDListOrStrOrNone = Field(None, alias='profileName')
    room_ids: UUIDListOrStrOrNone = Field(None, alias='roomId')
    specialties_code: UUIDListOrStrOrNone = Field(None, alias='specialtyCode')
    event_type: Union[List[EventType], EventType, None] = Field(None, alias='typeId')
    module: UUIDListOrStrOrNone = Field(
        None,
        alias='courseUnitRealizationId',
    )
    time_start: datetime = Field(..., alias='timeMin')
    time_end: datetime = Field(..., alias='timeMax')
    size: int = 500
    # NOTE:
    #  Если когда то будем делать возможность указать этот size, нужно позаботиться что бы он валидатором не делался листом

    # validators

    _values_must_be_in_list = validator('*', pre=False, allow_reuse=True)(value_must_be_in_list)

    class Config:
        json_encoders = {
            datetime: python_datetime_to_java,
        }


class EventRequestQuery(BaseRequest):
    """Represents a query for event request."""

    tz: str = 'Asia/Tyumen'
    auth_action: str = Field('', alias='authAction')
