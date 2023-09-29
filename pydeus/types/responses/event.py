from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Optional
from uuid import UUID

from pydantic import UUID4, BaseModel, Field, validator

from pydeus.types._validators import normalize_href_data, value_must_be_in_list
from pydeus.types.event import EventType
from pydeus.types.responses.base import BaseResponse
from pydeus.types.responses.module import ModuleResponseData
from pydeus.types.responses.person import PersonResponseData
from pydeus.types.responses.room import RoomResponseData
from pydeus.types.responses.training_team import TrainingTeamResponseData


class BaseEventResponseJson(BaseResponse):
    training_teams: Optional[List[TrainingTeamResponseData]] = Field(
        None,
        alias='cycle-realizations',
    )
    rooms: Optional[List[RoomResponseData]] = None
    event_rooms: Optional[List[EventRooms]] = Field(None, alias='event-rooms')
    attendees: Optional[List[EventAttendees]] = Field(None, alias='event-attendees')
    persons: Optional[List[PersonResponseData]] = None

    _values_must_be_in_list = validator(
        'modules', 'organizers', pre=True, allow_reuse=True, check_fields=False
    )(value_must_be_in_list)


class EventLinks(BaseModel):
    """Represents a links in event data."""

    type: EventType
    module: UUID4 = Field(..., alias='course-unit-realization')
    training_team: str = Field(..., alias='cycle-realization')
    room: UUID4 = Field(..., alias='location')
    duration: str
    team: str
    organizers: List[str]

    _organizer_must_be_list = validator('organizers', pre=True, allow_reuse=True)(
        value_must_be_in_list
    )


class EventResponseData(BaseResponse):
    """Represents event data in json response."""

    topic: Optional[str] = Field(None, alias='name')
    topic_type: Optional[str] = Field(None, alias='nameShort')
    state: str = Field(None, alias='holdingStatus')
    start: datetime
    end: datetime
    links: EventLinks = Field(..., alias='_links')
    id: UUID

    # validators
    _normilize_href_data = validator('links', pre=True, allow_reuse=True)(
        normalize_href_data,
    )

    @validator('state', pre=True)
    def _normilize_status_data(cls, status: Dict) -> str:
        return status.get('id')


class EventRoomsLinks(BaseModel):
    event_id: UUID = Field(..., alias='event')
    room_id: UUID = Field(..., alias='room')


class EventRooms(BaseModel):
    id: UUID4
    links: EventRoomsLinks = Field(..., alias='_links')

    _normilize_href_data = validator('links', pre=True, allow_reuse=True)(
        normalize_href_data,
    )


class EventOrginzerLinks(BaseModel):
    event_attendees: List[UUID4] = Field(..., alias='event-attendees')

    # validators
    _value_must_be_in_list = validator('event_attendees', pre=True, allow_reuse=True)(
        value_must_be_in_list
    )


class EventOrganizer(BaseModel):
    event_id: UUID = Field(..., alias='eventId')
    links: EventOrginzerLinks = Field(..., alias='_links')

    _normilize_href_data = validator('links', pre=True, allow_reuse=True)(
        normalize_href_data,
    )


class EventAttendeesLinks(BaseModel):
    person: UUID


class EventAttendees(BaseModel):
    id: UUID4
    links: EventAttendeesLinks = Field(..., alias='_links')

    _normilize_href_data = validator('links', pre=True, allow_reuse=True)(
        normalize_href_data,
    )


class EventResponseMulti(BaseEventResponseJson):
    """Represents a event response."""

    events: Optional[List[EventResponseData]] = None
    modules: Optional[List[ModuleResponseData]] = Field(
        None,
        alias='course-unit-realizations',
    )
    organizers: List[EventOrganizer] = Field(..., alias='event-organizers')


class EventResponseSingle(BaseEventResponseJson, EventResponseData):
    modules: Optional[List[ModuleResponseData]] = Field(
        None,
        alias='course-unit-realization',
    )
    organizers: List[EventOrganizer]
