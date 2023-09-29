class ModeusURL:
    """Represents Modeus URL's."""

    app_config_json = 'https://utmn.modeus.org/assets/app.config.json'
    oauth2 = 'https://auth.modeus.org/oauth2/authorize'
    commonauth = 'https://auth.modeus.org/commonauth'

    # API methods

    ## Events
    event = 'https://utmn.modeus.org/schedule-calendar-v2/api/calendar/events/'
    event_attendances = 'https://utmn.modeus.org/schedule-calendar-v2/api/calendar/events/{event_id}/person-attendances'
    events_search = 'https://utmn.modeus.org/schedule-calendar-v2/api/calendar/events/search'

    ## Search
    search_specialties = (
        'https://utmn.modeus.org/schedule-calendar-v2/api/curriculum/specialties/search'
    )
    search_learning_profile = (
        'https://utmn.modeus.org/schedule-calendar-v2/api/curriculum/profiles/search'
    )
    search_module = (
        'https://utmn.modeus.org/schedule-calendar-v2/api/courses/course-unit-realizations/search'
    )
    search_person = 'https://utmn.modeus.org/schedule-calendar-v2/api/people/persons/search'
    search_room = 'https://utmn.modeus.org/schedule-calendar-v2/api/campus/rooms/search'
    serach_training_team = (
        'https://utmn.modeus.org/schedule-calendar-v2/api/courses/cycle-realizations/search'
    )
