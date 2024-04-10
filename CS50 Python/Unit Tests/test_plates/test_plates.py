import pytest

from plates import is_valid

def test_first():
    assert is_valid("CS50") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("A12345") == False
    assert is_valid("123456") == False


def test_second():
    assert is_valid("MAXI") == True
    assert is_valid("lewis") == True
    assert is_valid("Sergio") == True
    assert is_valid("Penelope") == False
    assert is_valid("P") == False
    assert is_valid("pereZ50") == False
    assert is_valid("") == False


def test_third():
    assert is_valid("AB1234") == True
    assert is_valid("AB12") == True
    assert is_valid("dddd21") == True
    assert is_valid("lewis1") == True
    assert is_valid("lew1is") == False
    assert is_valid("le123s") == False
    assert is_valid("CS500A") == False
    assert is_valid("CS0500") == False
    assert is_valid("ABCDE0") == False


def test_fourth():
    assert is_valid("AB:--C") == False
    assert is_valid("AB500-") == False
    assert is_valid("AB50   ") == False
    assert is_valid("_abcde") == False
