from work import convert

def test():
    assert convert("9:60 AM to 5:60 PM") == False
    assert convert("9:59 AM to 5:59 PM") == True
