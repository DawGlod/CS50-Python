import pytest

from twttr import shorten

def test_argument():
    assert shorten("Twitter") == "Twttr"
    assert shorten("Mercedes") == "Mrcds"
    assert shorten("Red Bull") == "Rd Bll"


def test_corner():
    assert shorten("a") == ""
    assert shorten("www") == "www"
    assert shorten("AK47") == "K47"
    assert shorten("59837459834") == "59837459834"
    assert shorten("AGgdfagSv5") == "GgdfgSv5"
    assert shorten("Cs;Go") == "Cs;G"

