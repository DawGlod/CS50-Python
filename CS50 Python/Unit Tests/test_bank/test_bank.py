import pytest
from bank import value


def test_hello():
    assert value("Hello") == 0
    assert value("hello") == 0
    assert value("Hello, David!") == 0
    assert value("Hello Hello") == 0

def test_h():
    assert value("Hi") == 20
    assert value("Hermione") == 20
    assert value(" ho ho ") == 20
    assert value("h:") == 20

def test_other():
    assert value("What's up?") == 100
    assert value("Yo") == 100
    assert value("Maaan11") == 100
    assert value("1134") == 100
