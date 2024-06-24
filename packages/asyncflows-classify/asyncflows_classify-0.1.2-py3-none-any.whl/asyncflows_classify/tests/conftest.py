from tempfile import TemporaryDirectory

import pytest
from asyncflows.log_config import get_logger


@pytest.fixture(scope="function")
def log():
    return get_logger()


@pytest.fixture(scope="function")
def temp_dir():
    temp_dir = TemporaryDirectory()
    yield temp_dir.name
    temp_dir.cleanup()
