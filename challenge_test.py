"""Test functions in challenge.py."""
import pytest
from challenge import add_prefix_un, make_word_groups

# ===========test add_prefix_un===========
def test_add_prefix_un_returns_string() -> None:
    """Test that add_prefix_un returns a string."""
    assert isinstance(add_prefix_un("test"), str)

def test_add_prefix_un_returns_expected() -> None:
    """Test that add_prefix_un returns expected string."""
    assert add_prefix_un("happy") == "unhappy"
    assert add_prefix_un("manageable") == "unmanageable"


# ===========test make_word_groups===========
def test_make_word_groups_returns_string() -> None:
  """Test that make_word_groups returns a string."""
  assert isinstance(make_word_groups(["un", "believeavle", "remarkable", "ending"]), str)

@pytest.mark.parametrize(
      ("words", "expected"),
      [
         (["en", "close", "joy", "lighten"], "en :: enclose :: enjoy :: enlighten"),
         (["pre", "serve", "dispose", "position"], "pre :: preserve :: predispose :: preposition"),
         (["auto", "didactic", "graph", "mate"], "auto :: autodidactic :: autograph :: automate"),
         (["inter", "twine", "connected", "dependent"], "inter :: intertwine :: interconnected :: interdependent")

      ]
)
def test_make_word_groups_returns_expected(words: list, expected: str) -> None:
  """Test that make_word_groups returns expected string."""
  assert make_word_groups(words) == expected