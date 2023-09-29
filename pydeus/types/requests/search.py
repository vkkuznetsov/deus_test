from typing import List, Union

from pydantic import Field, validator

from pydeus.types._validators import value_must_be_in_list
from pydeus.types.requests.base_request import BaseRequest
from pydeus.types.sort import (
    SortLearingProfle,
    SortModule,
    SortPerson,
    SortRoom,
    SortSpecialties,
    SortTrainingTeam,
)


class BaseSearch(BaseRequest):
    """Represents a base search parameters.

    Args:
        page: int - page of search
        size: int - size of the search
        sort: str - how to sort the results
    """

    name: str
    page: int = 0
    size: int = 10
    sort: str


class SearchPerson(BaseSearch):
    """Represents a person search parameters.

    Args:
        name: str - part of the name or full name of the person
        page: int - page of search
        size: int - size of the search
        sort: SortPerson, str - how to sort the results
    """

    name: str = Field('', alias='fullName')
    sort: str = SortPerson.full_name.increase


class SearchTrainingTeam(BaseSearch):
    """Represents a training team search parameters.

    Args:
        name: str - part of the name or full name of the training team
        page: int - page of search
        size: int - size of the search
        sort: SortTrainingTeam, str - how to sort the results.
    """

    name: str = Field('', alias='fulltext')
    sort: str = SortTrainingTeam.name_short_code.increase


class SearchSpecialties(BaseSearch):
    """Represents a specialties search parameters.

    Args:
        name: str - part of the name or full name of the specialties
        page: int - page of search
        size: int - size of the search
        sort: SortSpecialties, str - how to sort the results.
    """

    name: str = Field('', alias='fullText')
    sort: str = SortSpecialties.code.increase


class SearchRoom(BaseSearch):
    """Represents a room search parameters.

    Args:
        name: str - part of the name or full name of the room
        page: int - page of search
        size: int - size of the search
        sort: SortSpecialties, str - how to sort the results.
    """

    sort: str = SortRoom.building_name.increase


class SearchLearningProfile(BaseSearch):
    """Represents a learning profile search parameters.

    Args:
        name: str - part of the name or full name of the learning profile
        page: int - page of search
        size: int - size of the search
        sort: SortLearingProfle, str - how to sort the results.
    """

    # TODO: Check what happens if list will have > 1 parameter
    name: Union[List[str], str]
    sort: str = SortLearingProfle.name.increase

    _name_must_be_list = validator('name', allow_reuse=True)(value_must_be_in_list)


class SearchModule(BaseSearch):
    """Represents a module search parameters."""

    sort: str = SortModule.name.increase
