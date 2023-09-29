from pydeus.types._converter import (
    EventConverter,
    LearnProfileConverter,
    ModuleConverter,
    PersonConverter,
    RoomConverter,
    SpecialtiesConverter,
    TrainingTeamConverter,
)
from pydeus.types.responses import (
    EventResponseMulti,
    LearnProfileResponse,
    ModuleResponse,
    PersonResponse,
    RoomResponse,
    SpecialtiesResponse,
    TrainingTeamResponse,
)
from tests._test_utils import check_model_values_is_not_none


def test_build_for_event_response(event_response):
    response_json = EventResponseMulti(**event_response)
    events = EventConverter(response_json).convert_list()
    assert events is not None
    first_event = events[0]
    check_model_values_is_not_none(first_event, exclude={'team'})


def test_build_specialties(specialties_response):
    response_json = SpecialtiesResponse(**specialties_response)
    specialties = SpecialtiesConverter(response_json).convert_list()
    assert specialties is not None
    first_specialty = specialties[0]
    check_model_values_is_not_none(first_specialty)


def test_build_room(room_response):
    response_json = RoomResponse(**room_response)
    room = RoomConverter(response_json).convert_list()
    assert room is not None
    first_room = room[0]
    check_model_values_is_not_none(first_room)


def test_build_module(module_response):
    response_json = ModuleResponse(**module_response)
    module = ModuleConverter(response_json).convert_list()
    assert module is not None
    first_module = module[0]
    check_model_values_is_not_none(first_module)


def test_build_person(person_response):
    response_json = PersonResponse(**person_response)
    person = PersonConverter(response_json).convert_list()
    assert person is not None
    first_person = person[0]
    check_model_values_is_not_none(first_person, exclude={'middle_name'})


def test_build_learn_profile(learning_profile_response):
    response_json = LearnProfileResponse(**learning_profile_response)
    learn_profile = LearnProfileConverter(response_json).convert_list()
    assert learn_profile is not None
    first_learn_profile = learn_profile[0]
    check_model_values_is_not_none(first_learn_profile)


def test_build_training_team(training_team_response):
    response_json = TrainingTeamResponse(**training_team_response)
    training_team = TrainingTeamConverter(response_json).convert_list()
    assert training_team is not None
    first_training_team = training_team[0]
    check_model_values_is_not_none(first_training_team)
