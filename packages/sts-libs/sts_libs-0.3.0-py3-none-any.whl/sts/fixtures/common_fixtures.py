from collections.abc import Generator

import pytest

from sts.utils.cmdline import run


@pytest.fixture()
def _log_check() -> Generator:
    """Checks if a new coredump entry was generated during the test."""
    last_dump = run('coredumpctl -1', msg='Checking dumps before test').stdout
    yield
    recent_dump = run('coredumpctl -1', msg='Checking dumps after test').stdout
    assert recent_dump == last_dump, 'New coredump appeared during the test'
