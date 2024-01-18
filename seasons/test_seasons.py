from seasons import convert
import pytest

def test_seasons():
    with pytest.raises(ValueError):
        convert("1999/12/13")
    assert convert("1999-12-")
