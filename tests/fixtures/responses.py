from typing import Dict

import pytest

from .response_generators.event_generator import generate_event_response
from .response_generators.search_generator import (
    LearningProfileGen,
    ModuleGen,
    PersonGen,
    RoomGen,
    SpecialtiesGen,
    TrainingTeamGen,
    generate_learning_profile_response,
    generate_module_response,
    generate_person_response,
    generate_room_response,
    generate_specialities_response,
    generate_training_team_response,
)


@pytest.fixture
def event_response() -> Dict:
    return generate_event_response()


@pytest.fixture
def specialties_response() -> Dict:
    params = [
        SpecialtiesGen('Математика и Изучение модеуса', '01.05.03'),
        SpecialtiesGen('Как писать правильно а неправильно не писать', '27.02.2023'),
    ]
    return generate_specialities_response(params)


@pytest.fixture
def learning_profile_response() -> Dict:
    params = [
        LearningProfileGen('Профиль 1', '01.05.03'),
        LearningProfileGen('Профиль 2', '27.02.2023'),
    ]
    return generate_learning_profile_response(params)


@pytest.fixture
def module_response() -> Dict:
    params = [
        ModuleGen('Pydeus как не нужно писать тесты?', 'Pкннпт'),
        ModuleGen('Дискретная математика', 'ДМ'),
    ]
    return generate_module_response(params)


@pytest.fixture
def person_response() -> Dict:
    params = [
        PersonGen('Велижанин', 'Игорь'),
        PersonGen('Земсков', 'Никита', 'Александрович'),
    ]
    return generate_person_response(params)


@pytest.fixture
def room_response() -> Dict:
    params = [
        RoomGen(
            room_name='422-2 (УЛК-05)',
            projector_available=True,
            building_name='УЛК-05',
            address='ул. Перекопская, 15а',
            capacity=13,
        ),
        RoomGen(
            room_name='317 (УЛК-04)',
            projector_available=False,
            building_name='УЛК-04',
            address='ул. Ленина, 16',
            capacity=21,
        ),
    ]
    return generate_room_response(params)


@pytest.fixture
def training_team_response() -> Dict:
    params = [
        TrainingTeamGen('Практическое занятие', 'П', 'ПиОА П-01.01', 'ПиОА'),
        TrainingTeamGen('Лекционное занятие', 'Л', 'КСТ19-9-1', 'КСТ'),
    ]
    return generate_training_team_response(params)
