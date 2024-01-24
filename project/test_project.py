from project_copy import Investment, collect_investment_data, get_input, get_compound, get_contribute
import pytest

def test_get_input(mocker):
    mocker.patch('builtins.input', return_value='1')
    assert get_input("Enter a number: ", int) == 1
    mocker.patch('builtins.input', return_value='a')
    with pytest.raises(ValueError):
        assert get_input("Enter a number: ", int) == 1
    # assert get_input("1", int) == 1
    # assert get_input("0.1", float) == 0.1
    # assert get_input("1", float) == 1
    # with pytest.raises(ValueError):
    #     assert get_input("a", float)
    # with pytest.raises(ValueError):
    #     assert get_input("a", int)
    # with pytest.raises(ValueError):
    #     assert get_input("1.0", int)


def test_function_2():
    ...


def test_function_n():
    ...
