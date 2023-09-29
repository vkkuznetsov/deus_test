from typing import TYPE_CHECKING, List, Optional

from pydeus.types._converter.abc import ABCConverter
from pydeus.types.search import Building, Room

if TYPE_CHECKING:
    from pydeus.types.responses.room import BuildingResponseData, RoomResponse, RoomResponseData


class RoomConverter(ABCConverter):
    def __init__(self, room_response: 'RoomResponse') -> None:
        self.room_response = room_response

    def convert_list(self) -> Optional[List[Room]]:
        if not self.room_response.rooms:
            return None

        return [self._build_one_room(room) for room in self.room_response.rooms]

    def _build_one_room(self, room: 'RoomResponseData') -> Room:
        building = self._build_one_building(room.building)
        return Room(
            id=room.id,
            room=room.name,
            project_available=room.project_availiable,
            building=building,
            capacity=room.capacity,
        )

    def _build_one_building(self, raw_building: 'BuildingResponseData') -> Building:
        return Building(
            id=raw_building.id,
            name=raw_building.name,
            address=raw_building.address,
        )
