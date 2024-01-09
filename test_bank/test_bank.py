from bank import value

def test_assert():
    assert value("Hello") == 0
    assert value("hello") == 0
    assert value("hot") == 20
    assert value("What’s up") == 100
