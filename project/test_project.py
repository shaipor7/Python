from project import get_input, get_compound, get_contribute, starting_term, dca_term, reinvestment
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

def test_starting_term():
    Input = [{'start': 1000, 'after': 10, 'return_rate': 10.0, 'compound': 12, 'addition': 100, 'contribute': 12}]
    assert starting_term(Input) == 2707.04

    Input = [{'start': 1000, 'after': 10, 'return_rate': 10.0, 'compound': 12, 'addition': 100, 'contribute': 12}
             , {'after': 10, 'return_rate': 10.0, 'compound': 12, 'addition': 100, 'contribute': 12}]
    assert starting_term(Input) == 7328.07

def test_dca_term():
    Input = [{'start': 1000, 'after': 10, 'return_rate': 10.0, 'compound': 12, 'addition': 100, 'contribute': 12}]
    assert dca_term(Input) == 20484.5

    Input = [{'start': 1000, 'after': 10, 'return_rate': 10.0, 'compound': 12, 'addition': 100, 'contribute': 12}
             , {'after': 10, 'return_rate': 10.0, 'compound': 12, 'addition': 100, 'contribute': 12}]
    assert dca_term(Input) == 75936.89

    Input = [{'start': 1000, 'after': 10, 'return_rate': 10.0, 'compound': 12, 'addition': 100, 'contribute': 12}
             , {'after': 10, 'return_rate': 10.0, 'compound': 12, 'addition': 100, 'contribute': 12}
             , {'after': 10, 'return_rate': 10.0, 'compound': 12, 'addition': 100, 'contribute': 12}]
    assert dca_term(Input) == 226048.80

    Input = [{'start': 1000, 'after': 1, 'return_rate': 10.0, 'compound': 12, 'addition': 100, 'contribute': 12}
             , {'after': 2, 'return_rate': 10.0, 'compound': 12, 'addition': 100, 'contribute': 12}
             , {'after': 3, 'return_rate': 10.0, 'compound': 12, 'addition': 100, 'contribute': 12}
             , {'after': 4, 'return_rate': 10.0, 'compound': 12, 'addition': 100, 'contribute': 12}]
    assert dca_term(Input) == 20484.50

    Input = [{'start': 1000, 'after': 5, 'return_rate': 10, 'compound': 12, 'addition': 1000, 'contribute': 12}
             , {'after': 2, 'return_rate': 5, 'compound': 12, 'addition': 500, 'contribute': 12}]
    assert dca_term(Input) == 98156.38
