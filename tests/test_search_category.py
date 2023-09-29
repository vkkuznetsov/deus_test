from pydeus.client import ModeusClient


async def test_search_specialties(mocked_api_client, specialties_response):
    client: ModeusClient = mocked_api_client(specialties_response)
    specialties = await client.search.specialties()
    assert specialties is not None


async def test_search_learning_profile(mocked_api_client, learning_profile_response):
    client: ModeusClient = mocked_api_client(learning_profile_response)
    learning_profile = await client.search.learn_profiles()
    assert learning_profile is not None


async def test_search_rooms(mocked_api_client, room_response):
    client: ModeusClient = mocked_api_client(room_response)
    rooms = await client.search.rooms()
    assert rooms is not None


async def test_search_modules(mocked_api_client, module_response):
    client: ModeusClient = mocked_api_client(module_response)
    modules = await client.search.modules()
    assert modules is not None


async def test_search_persons(mocked_api_client, person_response):
    client: ModeusClient = mocked_api_client(person_response)
    persons = await client.search.persons()
    assert persons is not None


async def test_search_training_teams(mocked_api_client, training_team_response):
    client: ModeusClient = mocked_api_client(training_team_response)
    training_teams = await client.search.training_teams()
    assert training_teams is not None
