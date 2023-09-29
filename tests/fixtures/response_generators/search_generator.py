from typing import Dict, List, NamedTuple, Optional
from uuid import UUID, uuid4


class SpecialtiesGen(NamedTuple):
    name: str
    code: str


class LearningProfileGen(NamedTuple):
    name: str
    speciality_id: str


class ModuleGen(NamedTuple):
    name: str
    name_short: str


class PersonGen(NamedTuple):
    last_name: str
    first_name: str
    middle_name: Optional[str] = None


class RoomGen(NamedTuple):
    room_name: str
    projector_available: bool
    building_name: str
    address: str
    capacity: int = 0


class TrainingTeamGen(NamedTuple):
    name: str
    name_short: str
    code: str
    module_name: str


def generate_specialities_response(specialties_params: List[SpecialtiesGen]) -> Dict:
    specialties = {
        'specialties': [_generate_one_spec_response(param) for param in specialties_params]
    }
    return _embedded_response(specialties)


def generate_learning_profile_response(profiles_params: List[LearningProfileGen]) -> List[Dict]:
    learning_profiles = {
        'profiles': [_generate_one_prof_response(param) for param in profiles_params]
    }
    return _embedded_response(learning_profiles)


def generate_module_response(modules_params: List[ModuleGen]) -> List[Dict]:
    quarter_uuid = uuid4()
    modules = {
        'course-unit-realizations': [
            _generate_one_module_response(param, quarter_uuid) for param in modules_params
        ]
    }
    modules.update({'planning-periods': [_generate_planing_period(quarter_uuid)]})
    return _embedded_response(modules)


def generate_person_response(response_params: List[PersonGen]) -> List[Dict]:
    persons = {'persons': [_generate_one_person_response(param) for param in response_params]}
    return _embedded_response(persons)


def generate_room_response(response_params: List[RoomGen]) -> List[Dict]:
    rooms = {'rooms': [_generate_one_room_response(param) for param in response_params]}
    return _embedded_response(rooms)


def generate_training_team_response(response_params: List[TrainingTeamGen]) -> List[Dict]:
    training_teams = {
        'cycle-realizations': [
            _generate_one_training_team_response(param) for param in response_params
        ]
    }
    return _embedded_response(training_teams)


def _generate_one_spec_response(params: SpecialtiesGen) -> Dict:
    return {
        'name': params.name,
        'code': params.code,
        'id': params.code,
    }


def _generate_one_prof_response(params: LearningProfileGen) -> Dict:
    return {
        'name': params.name,
        'specialtyId': params.speciality_id,
        'id': uuid4(),
    }


def _generate_one_module_response(params: ModuleGen, quarter_uuid: UUID) -> Dict:
    slash_quarter_uuid = '/' + str(quarter_uuid)
    links = {'planning-period': {'href': slash_quarter_uuid}}
    return {
        'name': params.name,
        'nameShort': params.name_short,
        'prototypeId': uuid4(),
        'id': uuid4(),
        '_links': links,
    }


def _generate_planing_period(quarter_uuid: UUID) -> Dict:
    return {
        'name': '2021-2022 учебный год',
        'id': quarter_uuid,
    }


def _generate_one_person_response(params: PersonGen) -> Dict:
    full_name = f'{params.last_name} {params.first_name} {params.middle_name if params.middle_name else ""}'
    return {
        'lastName': params.last_name,
        'firstName': params.first_name,
        'middleName': params.middle_name,
        'fullName': full_name,
        'id': uuid4(),
    }


def _generate_one_room_response(params: RoomGen) -> Dict:
    return {
        'name': params.room_name,
        'nameShort': params.room_name,
        'building': {
            'id': uuid4(),
            'name': params.building_name,
            'nameShort': params.building_name,
            'address': params.address,
        },
        'projector_available': params.projector_available,
        'totalCapacity': params.capacity,
        'WorkingCapacity': params.capacity,
        'id': uuid4(),
    }


def _generate_one_training_team_response(params: TrainingTeamGen) -> Dict:
    slash_uuid = '/' + str(uuid4())
    return {
        'name': params.name,
        'nameShort': params.name_short,
        'code': params.code,
        'courseUnitRealizationNameShort': params.module_name,
        '_links': {
            'course-unit-realization': {'href': slash_uuid},
        },
        'id': uuid4(),
    }


def _embedded_response(response: Dict) -> Dict:
    return {'_embedded': response}
