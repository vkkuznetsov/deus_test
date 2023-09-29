from typing import Dict, List


def generate_event_response() -> Dict:
    response = {}
    response['events'] = generate_3_events()
    response['cycle-realiztion'] = generate_cycle_realiztion()
    response['course-unit-realizations'] = generate_course_unit_realizations()
    response['event-rooms'] = generate_event_rooms()
    response['rooms'] = generate_rooms()
    response['event-organizers'] = generate_event_organizers()
    response['event-attendees'] = generate_event_attendees()
    response['persons'] = generate_persons()
    return {'_embedded': response}


def generate_3_events() -> List[Dict]:
    events = [generate_one_event_dict() for i in range(3)]
    return events


def generate_course_unit_realizations() -> List[Dict]:
    course_unit_realizations = {
        'name': 'Введение в сетевое и системное администрирование',
        'nameShort': 'ВвСИСА',
        'prototypeId': 'b24c39a4-24f4-44fd-85fc-b5ab8acd6fe2',
        '_links': {
            'planning-period': {
                'href': '/48330c54-40f4-4ed0-8e71-c853f55f9ed5',
            },
        },
        'id': 'd75ca1a5-49ac-42a3-8166-a642909023d1',
    }
    return [course_unit_realizations]


def generate_cycle_realiztion() -> List[Dict]:
    cycle_realization = (
        {
            'name': 'Лекционное занятие',
            'nameShort': 'Л',
            'code': 'ВвСИСА Л-01',
            'courseUnitRealizationNameShort': 'ВвСИСА',
            '_links': {
                'course-unit-realization': {
                    'href': '/d75ca1a5-49ac-42a3-8166-a642909023d1',
                },
            },
            'id': '1908d899-123c-4706-9fd9-c72ea3f0923f',
        },
    )
    return [cycle_realization]


def generate_rooms() -> List[Dict]:
    rooms = {
        'name': '317 (УЛК-05)',
        'nameShort': '317 (УЛК-05)',
        'building': {
            'id': '67548cd6-b68b-4500-b079-c78e49567b10',
            'name': 'УЛК-05',
            'nameShort': 'УЛК-05',
            'address': 'ул. Перекопская, 15а',
            'displayOrder': '4',
        },
        'projectorAvailable': False,
        'totalCapacity': 26,
        'workingCapacity': 26,
        '_links': {
            'type': {
                'href': '/a53b203d-f55c-4e5c-9c68-8838d4ebe46a',
            },
            'building': {
                'href': '"/67548cd6-b68b-4500-b079-c78e49567b10"',
            },
        },
        'id': 'a53b203d-f55c-4e5c-9c68-8838d4ebe46a',
    }
    return [rooms]


def generate_event_rooms() -> List[Dict]:
    event_rooms = {
        '_links': {
            'event': {
                'href': '/24c65a58-5001-4019-b1d6-e2d785fc68f3',
            },
            'room': {
                'href': '/a53b203d-f55c-4e5c-9c68-8838d4ebe46a',
            },
        },
        'id': '41c29eef-f262-40b8-ac0a-529bad24dfe5',
    }
    return [event_rooms]


def generate_event_attendees() -> List[Dict]:
    event_id = '/24c65a58-5001-4019-b1d6-e2d785fc68f3'
    attend_id = 'e40b6a10-e39b-45a9-bb49-709838eae824'
    event_attendees_1 = generate_one_event_attendees(
        event_id, '/e412e4d3-19d1-11e0-8351-101111111111', attend_id
    )
    event_attendees_2 = generate_one_event_attendees(
        event_id, '/bf9b2cda-c110-11ea-aef1-005056a29568', attend_id
    )
    return [event_attendees_1, event_attendees_2]


def generate_one_event_attendees(event_id: str, person_id: str, uuid_id: str) -> Dict:
    return {
        '_links': {
            'event': {
                'href': event_id,
            },
            'person': {
                'href': person_id,
            },
        },
        'id': uuid_id,
    }


def generate_persons() -> List[Dict]:
    person_1 = generate_one_person(
        'Велижанин Игорь Евгеньевич', person_id='bf9b2cda-c110-11ea-aef1-005056a29568'
    )
    person_2 = generate_one_person(
        'Земсков Никита', person_id='e412e4d3-19d1-11e0-8351-101111111111'
    )
    return [person_1, person_2]


def generate_one_person(fio: str, person_id: str) -> Dict:
    last_name, first_name, *middle_name = fio.split(' ')
    middle_name = middle_name[0] if middle_name else None
    return {
        'lastName': last_name,
        'firstName': first_name,
        'middleName': middle_name,
        'fullName': fio,
        'id': person_id,
    }


def generate_event_organizers() -> List[Dict]:
    event_organizers = {
        'eventId': '24c65a58-5001-4019-b1d6-e2d785fc68f3',
        '_links': {
            'event': {
                'href': '/24c65a58-5001-4019-b1d6-e2d785fc68f3',
            },
            'event-attendees': [
                {'href': '/e40b6a10-e39b-45a9-bb49-709838eae824'},
                {'href': '/2a74c4f5-4461-4fd5-a7cc-3e1e543a7629'},
            ],
        },
    }
    return [event_organizers]


def generate_one_event_dict() -> Dict:
    return {
        'name': 'Введине в разработку модеуса',
        'nameShort': 'Лекционное занятие 4',
        'description': None,
        'start': '2023-02-20T12:00:00+05:00',
        'end': '2023-02-20T13:30:00+05:00',
        'startsAtLocal': '2023-02-20T12:00:00',
        'endsAtLocal': '2023-02-20T13:30:00',
        'startsAt': '2023-02-20T07:00:00',
        'endsAt': '2023-02-20T08:30:00',
        'holdingStatus': {
            'id': 'HELD',
            'name': 'Проведено',
            'audModifiedAt': '2023-02-20T08:50:00.585502',
            'audModifiedBy': '89016df8-415d-11e7-a66e-bf75d30473c1',
            'audModifiedBySystem': True,
        },
        'lessonTemplateId': 'ebcf7262-69f2-412c-8c5d-fb6a124f1277',
        '__version': 22,
        '_links': {
            'type': {
                'href': 'LECT',
            },
            'course-unit-realization': {
                'href': '/d75ca1a5-49ac-42a3-8166-a642909023d1',
            },
            'cycle-realization': {
                'href': '/1908d899-123c-4706-9fd9-c72ea3f0923f',
            },
            'lesson-realization': {
                'href': '/90d8d83f-282a-488e-aa74-dc78ea8ae685',
            },
            'lesson-realization-team': {
                'href': '/4bd0c637-e56e-4905-9f56-53a1b7fa049c',
            },
            'lesson-realization-template': {
                'href': '/ebcf7262-69f2-412c-8c5d-fb6a124f1277',
            },
            'location': {
                'href': '/24c65a58-5001-4019-b1d6-e2d785fc68f3/location',
            },
            'duration': {
                'href': '/24c65a58-5001-4019-b1d6-e2d785fc68f3/duration',
            },
            'team': {
                'href': '/24c65a58-5001-4019-b1d6-e2d785fc68f3/team',
            },
            'organizers': {
                'href': '/24c65a58-5001-4019-b1d6-e2d785fc68f3/organizers',
            },
        },
        'id': '24c65a58-5001-4019-b1d6-e2d785fc68f3',
    }
