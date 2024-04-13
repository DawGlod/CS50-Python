import pytest

from working import convert

def test_normal_first():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("11:59 AM to 11:20 PM") == "11:59 to 23:20"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"

def test_normal_second():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:30 PM") == "09:00 to 17:30"
    assert convert("1:11 AM to 11:11 PM") == "01:11 to 23:11"

def test_random_input():
    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ValueError):
        convert("")
    with pytest.raises(ValueError):
        convert("   ")

def test_wrong_hour():
    with pytest.raises(ValueError):
        convert("13 AM to 13 PM")
    with pytest.raises(ValueError):
        convert("1:15 AM to 1:70 PM")
    with pytest.raises(ValueError):
        convert("13 AM to 1:00 PM")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM,")
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")
