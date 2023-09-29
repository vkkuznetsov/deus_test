from datetime import datetime
from typing import List, Optional, Union
from uuid import UUID

from pydeus.api._base import BaseAPICategory
from pydeus.types._converter import EventConverter, EventTeamConverter
from pydeus.types.event import Event, EventType
from pydeus.types.person import Person
from pydeus.types.requests.event import EventRequestJson, EventRequestQuery
from pydeus.types.responses.attendances import EventTeamResponse
from pydeus.types.responses.event import EventResponseMulti, EventResponseSingle
from pydeus.types.urls import ModeusURL


class TimetableAPICategory(BaseAPICategory):
    """Represents search Modeus's API category."""

    async def events(
        self,
        range_from: datetime,
        range_to: datetime,
        persons: Union[UUID, List[UUID]] = None,
        teams: Union[UUID, List[UUID]] = None,
        years: Union[int, List[int]] = None,
        profiles: Union[str, List[str]] = None,
        specialty_codes: Union[str, List[str]] = None,
        lesson_types: Union[EventType, List[EventType]] = None,
        rooms: Union[UUID, List[UUID]] = None,
        module: Union[UUID, List[UUID]] = None,
        *,
        filter_model: Optional[object] = None,  # noqa: ARG002 unused argument
    ) -> List[Event]:
        """
        Get the timetable events.

        Args:
            year: int or list of ints
            team: UUID or list of UUIDs
            specialty_code: str or list of strs
            room: UUID or list of UUIDs
            profile: str or list of strs
            persons: UUID or list of UUIDs
            course_unit: UUID or list of UUIDs
            lesson_type: str or list of strs
            range_from: datetime
            range_to: datetime
            filter_model: object
        """
        query = EventRequestQuery().dict(by_alias=True)
        request_body = self._build_event_request_json(
            range_from=range_from,
            range_to=range_to,
            persons=persons,
            teams=teams,
            years=years,
            profiles=profiles,
            specialty_codes=specialty_codes,
            lesson_types=lesson_types,
            rooms=rooms,
            module=module,
        )

        response = await self.client.api_client.request(
            endpoint=ModeusURL.events_search,
            method='POST',
            query_params=query,
            payload=request_body,
            response_model=EventResponseMulti,
        )
        return EventConverter(response).convert_list()

    async def event(self, event_id: Union[UUID, str]) -> Optional[Event]:
        """
        Get the timetable event

        Args:
            event_id: UUID, str
        """
        endpoint = ModeusURL.event + event_id
        response = await self.client.api_client.request(
            endpoint=endpoint,
            method='GET',
            response_model=EventResponseSingle,
        )
        team = await self.team(event_id)
        return EventConverter(response).convert_one(team)

    async def team(self, event_id: Union[UUID, str]) -> List[Person]:
        """Get the team of event

        Args:
            event_id: UUID, str
        """
        endpoint = ModeusURL.event_attendances.format(event_id=event_id)
        response = await self.client.api_client.request(
            endpoint=endpoint,
            method='GET',
            response_model=EventTeamResponse,
        )
        return EventTeamConverter(response).convert_list()

    def _build_event_request_json(
        self,
        range_from: datetime,
        range_to: datetime,
        persons: Union[UUID, List[UUID]] = None,
        teams: Union[UUID, List[UUID]] = None,
        years: Union[int, List[int]] = None,
        profiles: Union[str, List[str]] = None,
        specialty_codes: Union[str, List[str]] = None,
        lesson_types: Union[EventType, List[EventType]] = None,
        rooms: Union[UUID, List[UUID]] = None,
        module: Union[UUID, List[UUID]] = None,
    ) -> EventRequestJson:
        return EventRequestJson(
            time_start=range_from,
            time_end=range_to,
            person_ids=persons,
            learning_teams=teams,
            years=years,
            profiles=profiles,
            specialties_code=specialty_codes,
            event_type=lesson_types,
            room_ids=rooms,
            module=module,
        ).json(by_alias=True, exclude_none=True)
