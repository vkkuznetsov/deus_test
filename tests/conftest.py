import pytest

pytest_plugins = [
    'tests.fixtures.client',
    'tests.fixtures.credentials',
    'tests.fixtures.responses',
]


def pytest_configure(config):
    config.addinivalue_line('markers', 'with_env: mark test which needed env variables')


def pytest_addoption(parser):
    parser.addoption(
        '--with-env',
        action='store_true',
        default=False,
        help='Run test which nedeed a env variables',
    )


def pytest_runtest_setup(item):
    if ('with_env' in item.keywords) and not (item.config.getoption('--with-env')):
        pytest.skip('Need --with-env to run')
