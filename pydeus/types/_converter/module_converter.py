from typing import TYPE_CHECKING, List, Optional

from pydeus.types._converter.abc import ABCConverter
from pydeus.types.search import Module, PlaningPeriod

if TYPE_CHECKING:
    from pydeus.types.responses.module import ModuleResponse, ModuleResponseData, PlaningPeriodData


class ModuleConverter(ABCConverter):
    def __init__(self, response_module: 'ModuleResponse') -> None:
        self.response_module = response_module

    def convert_list(self) -> List[Module]:
        if not self.response_module.modules:
            return None

        return [self._build_one_module(module) for module in self.response_module.modules]

    def _build_one_module(self, module: 'ModuleResponseData') -> Module:
        planing_period = self._build_one_planing_period(module)
        return Module(
            id=module.id,
            name=module.name,
            name_short=module.name_short,
            planing_periods=planing_period,
        )

    def _build_one_planing_period(self, module: 'ModuleResponseData') -> Optional[PlaningPeriod]:
        raw_planing_period = self._find_planing_period(module)
        return PlaningPeriod(
            id=raw_planing_period.id,
            name=raw_planing_period.name,
        )

    def _find_planing_period(self, module: 'ModuleResponseData') -> 'PlaningPeriodData':
        for planning_period in self.response_module.planning_periods:
            if planning_period.id == module.links.planning_period:
                return planning_period
