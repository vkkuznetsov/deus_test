from typing import TYPE_CHECKING, List, Optional

from pydeus.types._converter.abc import ABCConverter
from pydeus.types.person import Person

if TYPE_CHECKING:
    from pydeus.types.responses.attendances import EventTeamResponse


class EventTeamConverter(ABCConverter):
    def __init__(self, response_attendances: List['EventTeamResponse']) -> None:
        self.response_attendances = response_attendances

    def convert_list(self) -> Optional[List[Person]]:
        if not self.response_attendances:
            return None

        persons = [
            self._build_one_person(attendances)
            for attendances in self.response_attendances
            if attendances.role_id.value
            != 'TEACH'  # Не лучшее место для расположения != TEACH, но пока хз.
        ]  # Этот подразумевает то, что вернется только команда, для учителей другой метод
        return persons

    def _build_one_person(self, attendances: 'EventTeamResponse') -> Person:
        return Person(
            id=attendances.person_id,
            first_name=attendances.first_name,
            last_name=attendances.last_name,
            middle_name=attendances.middle_name,
            full_name=attendances.full_name,
        )
