from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import List, Optional, Union

from pydeus.types.base import Base
from pydeus.types.person import Person
from pydeus.types.search import Room


class EventType(Enum):
    """Represents a types of event."""

    lection = 'LECT'
    practice = 'SEMI'
    laboratory = 'LAB'
    attestation = 'MID_CHECK'
    final_certification = 'FINAL_CHECK'
    other = 'EVENT_OTHER'
    sefl_working = 'SELF'
    current_control = 'CUR_CHECK'


class EventState(Enum):
    """Represents a states of event."""

    not_started = 'DRAFT'
    started = 'DRAFT'
    ended = 'Ended'


class Event(Base):
    """Represents a Modeus event.

    Args:
        id: Event UUID
        module: Learning module
        module_short: Short name of module
        topic: Topic of the event
        type: Type of event (lection, lab, etc)
        location: Location of the event
        duration: Duration of the event in minutes
        start: Event start time
        end: Event end time
        state: State of the event
        organizers: List of organizations (teachers)
        team: Your team List for this event
    """

    module: str
    module_short: Optional[str] = None
    topic: str
    type: EventType
    room: Optional[Room] = None
    duration: int
    start: datetime
    end: datetime
    state: str
    organizers: Optional[List[Person]] = None
    team: Optional[List[Person]] = None

    @property
    def organizer(self) -> Union[str, None]:
        if self.organizers:
            return self.organizers[0]
        return None
