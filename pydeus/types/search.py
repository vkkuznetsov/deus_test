from uuid import UUID

from pydeus.types.base import Base


class Specialties(Base):
    name: str
    code: str
    id: str


class LearnProfile(Base):
    name: str
    speciality_code: str


class PlaningPeriod(Base):
    name: str  # TODO: Пока строка, потом можно и улучшить например, написать year start year end и тп


class Module(Base):
    name: str
    name_short: str
    planing_periods: PlaningPeriod


class Building(Base):
    name: str
    address: str


class Room(Base):
    room: str
    capacity: int
    project_available: bool
    building: Building


class TrainingTeam(Base):
    lesson_type: str
    lesson_type_short: str
    code: str
    module_short_name: str
    module_id: UUID
