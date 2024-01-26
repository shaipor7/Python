from project_copy import get_input, get_compound, get_contribute, income_invest_accumulate, addition, reinvestment
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
    assert income_invest_accumulate(Input) == 2707.04

    Input = [{'start': 1000, 'after': 10, 'return_rate': 10.0, 'compound': 12, 'addition': 100, 'contribute': 12}
             , {'after': 10, 'return_rate': 10.0, 'compound': 12, 'addition': 100, 'contribute': 12}]
    assert income_invest_accumulate(Input) == 7328.07

def test_addition():
    # Input = [{'start': 1000, 'after': 10, 'return_rate': 10.0, 'compound': 12, 'addition': 100, 'contribute': 12}]
    # assert addition(Input) == 20484.5

    Input = [{'start': 1000, 'after': 10, 'return_rate': 10.0, 'compound': 12, 'addition': 100, 'contribute': 12}
             , {'after': 10, 'return_rate': 10.0, 'compound': 12, 'addition': 100, 'contribute': 12}]
    assert addition(Input) == 83264.96
    ...

