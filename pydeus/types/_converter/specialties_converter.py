from typing import TYPE_CHECKING, List, Optional

from pydeus.types._converter.abc import ABCConverter
from pydeus.types.search import Specialties

if TYPE_CHECKING:
    from pydeus.types.responses.specialties import SpecialtiesResponse, SpecialtiesResponseData


class SpecialtiesConverter(ABCConverter):
    def __init__(self, response_specialties: 'SpecialtiesResponse') -> None:
        self.response_specialties = response_specialties

    def convert_list(self) -> Optional[List[Specialties]]:
        if not self.response_specialties.specialties:
            return None

        return [
            self._build_one_specialties(specialit)
            for specialit in self.response_specialties.specialties
        ]

    def _build_one_specialties(self, specialities: 'SpecialtiesResponseData') -> Specialties:
        return Specialties(
            name=specialities.name,
            code=specialities.code,
            id=specialities.id,
        )
