import sys

import httpx

from pydeus.client import ModeusClient

__all__ = ['ModeusClient']


__version__ = '0.0.1'
user_agent_header = 'PyDeus ({0}) Python/{1[0]}.{1[1]} httpx/{2}'.format(
    'https://github.com/AltDeus/pydeus {0}'.format(
        __version__,
    ),
    sys.version_info,
    httpx.__version__,
)
