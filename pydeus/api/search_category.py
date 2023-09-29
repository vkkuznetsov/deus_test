from typing import List, Optional

from pydeus.api._base import BaseAPICategory
from pydeus.types import (
    LearnProfile,
    Module,
    Person,
    Room,
    SortLearingProfle,
    SortModule,
    SortPerson,
    SortRoom,
    SortSpecialties,
    SortTrainingTeam,
    Specialties,
    TrainingTeam,
)
from pydeus.types._converter import (
    LearnProfileConverter,
    ModuleConverter,
    PersonConverter,
    RoomConverter,
    SpecialtiesConverter,
    TrainingTeamConverter,
)
from pydeus.types.requests.search import (
    SearchLearningProfile,
    SearchModule,
    SearchPerson,
    SearchRoom,
    SearchSpecialties,
    SearchTrainingTeam,
)
from pydeus.types.responses import (
    LearnProfileResponse,
    ModuleResponse,
    PersonResponse,
    RoomResponse,
    SpecialtiesResponse,
    TrainingTeamResponse,
)
from pydeus.types.urls import ModeusURL


class SearchAPICaterogry(BaseAPICategory):
    async def specialties(
        self,
        name: str = '',
        sort: str = SortSpecialties.code.increase,
        size: int = 10,
        page: int = 0,
    ) -> Optional[List[Specialties]]:
        request_body = SearchSpecialties(
            name=name,
            sort=sort,
            size=size,
            page=page,
        ).json(by_alias=True, exclude_none=True)

        response = await self.client.api_client.request(
            ModeusURL.search_specialties,
            'POST',
            response_model=SpecialtiesResponse,
            payload=request_body,
        )
        return SpecialtiesConverter(response).convert_list()

    async def learn_profiles(
        self,
        name: str = '',
        sort: str = SortLearingProfle.name.increase,
        size: int = 10,
        page: int = 0,
    ) -> Optional[List[LearnProfile]]:
        request_body = SearchLearningProfile(
            name=name,
            sort=sort,
            size=size,
            page=page,
        ).json(by_alias=True, exclude_none=True)

        response = await self.client.api_client.request(
            ModeusURL.search_learning_profile,
            'POST',
            response_model=LearnProfileResponse,
            payload=request_body,
        )
        return LearnProfileConverter(response).convert_list()

    async def modules(
        self,
        name: str = '',
        sort: str = SortModule.name.increase,
        size: int = 10,
        page: int = 0,
    ) -> Optional[List[Module]]:
        request_body = SearchModule(
            name=name,
            sort=sort,
            size=size,
            page=page,
        ).json(by_alias=True, exclude_none=True)

        response = await self.client.api_client.request(
            ModeusURL.search_module,
            'POST',
            response_model=ModuleResponse,
            payload=request_body,
        )
        return ModuleConverter(response).convert_list()

    async def persons(
        self,
        name: str = '',
        sort: str = SortPerson.full_name.increase,
        size: int = 10,
        page: int = 0,
    ) -> Optional[List[Person]]:
        request_body = SearchPerson(
            name=name,
            sort=sort,
            size=size,
            page=page,
        ).json(by_alias=True, exclude_none=True)

        response = await self.client.api_client.request(
            ModeusURL.search_person,
            'POST',
            response_model=PersonResponse,
            payload=request_body,
        )
        return PersonConverter(response).convert_list()

    async def rooms(
        self,
        name: str = '',
        sort: str = SortRoom.building_name.increase,
        size: int = 10,
        page: int = 0,
    ) -> Optional[List[Room]]:
        request_body = SearchRoom(
            name=name,
            sort=sort,
            size=size,
            page=page,
        ).json(by_alias=True, exclude_none=True)

        response = await self.client.api_client.request(
            ModeusURL.search_room,
            'POST',
            response_model=RoomResponse,
            payload=request_body,
        )
        return RoomConverter(response).convert_list()

    async def training_teams(
        self,
        name: str = '',
        sort: str = SortTrainingTeam.name_short_code.increase,
        size: int = 10,
        page: int = 0,
    ) -> Optional[List[TrainingTeam]]:
        request_body = SearchTrainingTeam(
            name=name,
            sort=sort,
            size=size,
            page=page,
        ).json(by_alias=True, exclude_none=True)

        response = await self.client.api_client.request(
            ModeusURL.serach_training_team,
            'POST',
            response_model=TrainingTeamResponse,
            payload=request_body,
        )
        return TrainingTeamConverter(response).convert_list()
