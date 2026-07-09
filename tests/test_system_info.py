from core.system_info import get_os


def test_get_os_returns_string():
    assert isinstance(get_os(), str)


