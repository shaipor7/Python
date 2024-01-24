from project_copy import Information, Investment
import pytest

def test_get_input():
    information = Information()
    assert information.get_input("1", int) == 1
    assert information.get_input("0.1", float) == 0.1
    assert information.get_input("1", float) == 1
    with pytest.raises(ValueError):
        assert information.get_input("a", float)
    with pytest.raises(ValueError):
        assert information.get_input("a", int)
    with pytest.raises(ValueError):
        assert information.get_input("1.0", int)


def test_function_2():
    ...


def test_function_n():
    ...
