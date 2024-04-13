import pytest

from numb3rs import validate

def test_validate():
    assert validate("12.44.3.244") == True
    assert validate("0.44.3.244") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("12.44.3.244.") == False
    assert validate("hi12.44.3.244.") == False
    assert validate("280.25.75.38") == False
    assert validate("28.26.275.38") == False
    assert validate("-13.44.3.255") == False
    assert validate("random_text") == False
