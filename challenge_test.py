"""Test functions in challenge.py."""
from challenge import add_prefix_un

def test_add_prefix_un_returns_string() -> None:
    """Test that add_prefix_un returns a string."""
    assert isinstance(add_prefix_un("test"), str)

def test_add_prefix_un_returns_expected() -> None:
    """Test that add_prefix_un returns expected string."""
    assert add_prefix_un("happy") == "unhappy"
    assert add_prefix_un("manageable") == "unmanageable"
