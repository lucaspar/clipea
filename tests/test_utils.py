"""Utils tests"""

from clipea import utils


def test_anystr_force_str() -> None:
    """Basic test for anystr_force_str()"""
    assert utils.anystr_force_str(b"hello") == "hello"
    assert utils.anystr_force_str("hello") == "hello"
