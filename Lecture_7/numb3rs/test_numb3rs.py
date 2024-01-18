from numb3rs import validate

def test():
    assert validate("1.2.3.4") == True
    assert validate("cat") == False
    assert validate("265.2.3.4") == False
    assert validate("192.168.0.256") == False  # Out of range octet

