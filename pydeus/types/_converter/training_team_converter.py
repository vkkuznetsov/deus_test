from typing import TYPE_CHECKING, List, Optional

from pydeus.types._converter.abc import ABCConverter
from pydeus.types.search import TrainingTeam

if TYPE_CHECKING:
    from pydeus.types.responses.training_team import TrainingTeamResponse, TrainingTeamResponseData


class TrainingTeamConverter(ABCConverter):
    def __init__(self, response_training_team: 'TrainingTeamResponse') -> None:
        self.response_training_team = response_training_team

    def convert_list(self) -> Optional[List[TrainingTeam]]:
        if not self.response_training_team.teams:
            return None

        return [
            self._build_one_training_team(response_training_team)
            for response_training_team in self.response_training_team.teams
        ]

    def _build_one_training_team(
        self, raw_training_team: 'TrainingTeamResponseData'
    ) -> TrainingTeam:
        return TrainingTeam(
            id=raw_training_team.id,
            lesson_type=raw_training_team.type_name,
            lesson_type_short=raw_training_team.name_short,
            code=raw_training_team.code,
            module_short_name=raw_training_team.module_short_name,
            module_id=raw_training_team.links.module,
        )
