from um import count

def test_assert():
    assert count("um") == 1
    assert count("yum") == 0
    assert count("UM") == 1
