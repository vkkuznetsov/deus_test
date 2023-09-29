from datetime import datetime
from typing import Dict, List, Union


def value_must_be_in_list(value: Union[List, str, datetime, None]) -> List[str]:
    if value is None:
        return None
    if isinstance(value, datetime):
        return value
    if not isinstance(value, list):
        return [value]
    return value


def normalize_href_data(values: Dict) -> Dict:
    """Validate events href's.

    Response data with events have a href's,
    but in the basic representation it's dict[dict(href=`value`)].

    Args:
        values: dict - event links

    Returns:
        dict

    Examples:
        >>> value = {type: {href: '/SEMI'}}
        >>> normilize_href_data(value)  # {type: SEMI}
        >>> value = {location: {href: '/71d5c2a7-4b80-4255-8eb4-21d6b803dcd0/location'}}
        >>> normilize_href_data(value) # {location: 71d5c2a7-4b80-4255-8eb4-21d6b803dcd0}
    """
    new_data = {}
    for k, v in values.items():
        if isinstance(v, list):
            href = _href_from_list(v)
        else:
            href = _href_from_one(v)
        new_data[k] = href
    return new_data


def _href_from_list(values: List[Dict[str, List[str]]]) -> List[str]:
    hrefs = []
    for value in values:
        href = _href_from_one(value)
        hrefs.append(href)
    return hrefs


def _href_from_one(value: Dict[str, str]) -> str:
    href: str = value.get('href')
    if href and len(href) > 1:
        if href[0] == '/':
            href = href.replace('/', '', 1)
    end_uuid_pos = href.find('/')
    if end_uuid_pos != -1:
        href = href[0:end_uuid_pos]
    return href
