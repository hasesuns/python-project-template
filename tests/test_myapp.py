import pytest

from myapp import __version__


@pytest.mark.github_actions
def test_version():
    assert __version__ == "0.1.0"
