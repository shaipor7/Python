from seasons import convert
import pytest

def test_seasons():
    with pytest.raises(SystemExit):
        convert("1999/12/13")
