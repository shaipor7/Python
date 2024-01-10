from plates import is_valid

def test_assert():
    assert is_valid("h") == False #lenght
    assert is_valid("123") == False #start with alphabetical
    assert is_valid("HO12KO") == False #number placement
    assert is_valid('ABC012') == False # zero
    assert is_valid('ABC,13') == False # alphanumeric


