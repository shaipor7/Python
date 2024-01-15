from working import convert

def test():
    # with pytest.raises(ValueError):
    #     convert("9:60 AM to 5:60 PM")
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
