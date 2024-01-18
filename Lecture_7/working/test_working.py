from working import convert
import pytest

def test():
    with pytest.raises(ValueError):
        convert("9 AM 5 PM")
    with pytest.raises(ValueError):
        convert("9:60 AM to 18:90 PM")
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
