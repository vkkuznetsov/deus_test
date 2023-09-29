from datetime import datetime

from pydeus.client import ModeusClient


async def test_events(mocked_api_client, event_response):
    client: ModeusClient = mocked_api_client(event_response)
    time = datetime.now()
    events = await client.timetable.events(time, time)
    assert events is not None
