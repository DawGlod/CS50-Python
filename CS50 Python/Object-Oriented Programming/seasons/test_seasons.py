import pytest
from seasons import Birthday

def test_basic():
    bd = Birthday("2003-07-06")
    assert bd.time_since_birthday_in_minutes_in_words() == "Ten million, nine hundred thirty-one thousand forty minutes"

def test_invalid_date():
    with pytest.raises(SystemExit):
        bd = Birthday("January 1st")
