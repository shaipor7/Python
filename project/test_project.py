from project_copy import Investment, collect_investment_data, get_input, get_compound, get_contribute
import pytest

def test_get_input(mocker):
    mocker.patch('builtins.input', side_effect=['ABC', '1', '1.0' , '0.1'])

    result_int = get_input("Enter a number: ", int)
    assert result_int == 1

    result_float = get_input("Enter a float: ", int)
    assert result_float == 1

    result_float = get_input("Enter a float: ", int)
    assert result_float == 1
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
