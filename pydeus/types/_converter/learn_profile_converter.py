from typing import TYPE_CHECKING, List, Optional

from pydeus.types._converter.abc import ABCConverter
from pydeus.types.search import LearnProfile

if TYPE_CHECKING:
    from pydeus.types.responses import LearningProfileResponseData, LearnProfileResponse


class LearnProfileConverter(ABCConverter):
    def __init__(self, response_learn_profle: 'LearnProfileResponse') -> None:
        self.response_learn_profile = response_learn_profle

    def convert_list(self) -> Optional[List[LearnProfile]]:
        if not self.response_learn_profile.profiles:
            return None

        return [
            self._build_one_learn_profile(response_learn_profile)
            for response_learn_profile in self.response_learn_profile.profiles
        ]

    def _build_one_learn_profile(
        self, response_learn_profile: 'LearningProfileResponseData'
    ) -> LearnProfile:
        return LearnProfile(
            id=response_learn_profile.id,
            name=response_learn_profile.name,
            speciality_code=response_learn_profile.specialties_code,
        )
