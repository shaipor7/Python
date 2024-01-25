from project_copy import Investment, collect_investment_data, get_input, get_compound, get_contribute
import pytest

def test_get_input(mocker):
    mocker.patch('builtins.input', side_effect=['ABC', '1', '1' , '0.1'])
    assert get_input("Enter: ", int) == 1
    assert get_input("Enter: ", float) == 1
    assert get_input("Enter: ", float) == 0.1

def test_get_compound(mocker):
    mocker.patch('builtins.input', side_effect=['a', '0', 'monthly'])
    assert get_compound("Enter: ") == 1
    assert get_compound("Enter: ") == 12

def test_get_contribute(mocker):
    mocker.patch('builtins.input', side_effect=['m', '0', 'year'])
    assert get_contribute("Enter: ") == 12
    assert get_contribute("Enter: ") == 1

def test_income_invest_accumulate():
    Input = [{'start': 1000, 'after': 10, 'return_rate': 10.0, 'compound': 12, 'addition': 100, 'contribute': 12}]
    Invest = Investment(Input)
    assert Invest.income_invest_accumulate() == 2707.04

def
