from typing import TYPE_CHECKING, List, Optional, Union

from pydeus.types import Person, Room
from pydeus.types._converter.abc import ABCConverter
from pydeus.types.event import Event

if TYPE_CHECKING:
    from pydeus.types.responses.event import (
        EventResponseData,
        EventResponseMulti,
        EventResponseSingle,
    )
    from pydeus.types.responses.module import ModuleResponseData


class EventConverter(ABCConverter):
    def __init__(self, response_events: Union['EventResponseSingle', 'EventResponseMulti']):
        self.response_json = response_events

    def convert_list(self) -> Optional[List[Event]]:
        if not self.response_json or not self.response_json.events:
            return None
        events = []

        for event in self.response_json.events:
            event_model = self._build_one_event(event)
            events.append(event_model)
        return events

    def convert_one(self, team: Optional[List[Person]] = None) -> Optional[Event]:
        if not self.response_json:
            return None

        event = self.response_json
        event_model = self._build_one_event(event, team)
        return event_model

    def _build_one_event(
        self, event: 'EventResponseData', team: Optional[List[Person]] = None
    ) -> Event:
        event_module = self._find_event_module(event)
        event_room = self._find_event_room(event)
        event_organizers = self._find_event_organizer(event)
        event_duration = (event.end - event.start).total_seconds()

        return Event(
            id=event.id,
            module=event_module.name,
            module_short=event_module.name_short,
            topic=event.topic,
            type=event.links.type,
            room=event_room,
            duration=event_duration,
            start=event.start,
            end=event.end,
            state=event.state,
            organizers=event_organizers,
            team=team,
        )

    def _find_event_module(self, event: 'EventResponseData') -> 'ModuleResponseData':
        for module in self.response_json.modules:
            if module.id == event.links.module:
                return module

    def _find_event_room(self, event: 'EventResponseData') -> Optional[Room]:
        event_room_id = None
        for event_room in self.response_json.event_rooms:
            if event_room.links.event_id == event.links.room:
                event_room_id = event_room.links.room_id

        if not event_room_id:
            return None

        for room in self.response_json.rooms:
            if room.id == event_room_id:
                return Room(
                    id=room.id,
                    room=room.name,
                    capacity=room.capacity,
                    project_available=room.project_availiable,
                    building=room.building,
                )
        return None

    def _find_event_organizer(self, event: 'EventResponseData') -> Optional[List[Person]]:
        event_organizer = []
        event_attendees_ids = None
        for organizer in self.response_json.organizers:
            if organizer.event_id == event.id:
                event_attendees_ids = organizer.links.event_attendees
        if not event_attendees_ids:
            return None

        event_persons_ids = []
        for event_attend in self.response_json.attendees:
            if event_attend.id in event_attendees_ids:
                event_persons_ids.append(event_attend.links.person)
        if not event_persons_ids:
            return None

        for person in self.response_json.persons:
            if person.id in event_persons_ids:
                event_organizer.append(person)
        return event_organizer
