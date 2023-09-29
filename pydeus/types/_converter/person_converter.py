from typing import TYPE_CHECKING, List, Optional

from pydeus.types._converter.abc import ABCConverter
from pydeus.types.person import Person

if TYPE_CHECKING:
    from pydeus.types.responses.person import PersonResponse, PersonResponseData


class PersonConverter(ABCConverter):
    def __init__(self, person_response: 'PersonResponse') -> None:
        self.person_response = person_response

    def convert_list(self) -> Optional[List[Person]]:
        if not self.person_response.persons:
            return None

        return [self._build_one_person(person) for person in self.person_response.persons]

    def _build_one_person(self, raw_person: 'PersonResponseData') -> Person:
        return Person(
            id=raw_person.id,
            first_name=raw_person.first_name,
            last_name=raw_person.last_name,
            middle_name=raw_person.middle_name,
            full_name=raw_person.full_name,
        )
