import pytest

from um import count

def test_typical():
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2

def test_starting():
    assert count("umbrella?") == 0
    assert count("want some um umbrella?") == 1
    assert count("ummmm") == 0

def test_ending():
    assert count("gravittum") == 0
    assert count("i have a copium") == 0
    assert count("Chris Lulhum") == 0


def test_random_input():
    assert count("") == 0
    assert count("um umu umu umum um") == 2
    assert count(":))))") == 0

def test_numbers():
    assert count("1") == 0
    assert count("33") == 0
    assert count("0") == 0


