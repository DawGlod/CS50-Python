import pytest

from project import getSessionTime, calculateRaceTime, calculateLaps, calculateFuel, display

def test_getSessionTime(mocker):
    mocker.patch('builtins.input', side_effect=[1, 30, 0])
    assert getSessionTime() == 5400

    mocker.patch('builtins.input', side_effect=[0, 45, 30])
    assert getSessionTime() == 2730

    mocker.patch('builtins.input', side_effect=[2, 59, 59])
    assert getSessionTime() == 10799

def test_calculateRaceTime(mocker):
    mocker.patch('builtins.input', side_effect=[1, 30, 500])
    assert calculateRaceTime() == 90.5

    mocker.patch('builtins.input', side_effect=[0, 45, 250])
    assert calculateRaceTime() == 45.25

    mocker.patch('builtins.input', side_effect=[2, 0, 0])
    assert calculateRaceTime() == 120

def test_calculateLaps():
    assert calculateLaps(5400, 90.5) == 60
    assert calculateLaps(2730, 45.25) == 61
    assert calculateLaps(3600, 60) == 60

def test_calculateFuel(mocker):
    mocker.patch('builtins.input', side_effect=[2, 'n'])
    assert calculateFuel(60) == 120

    mocker.patch('builtins.input', side_effect=[2, 'y'])
    assert calculateFuel(60) == 122

    mocker.patch('builtins.input', side_effect=[1.5, 'n'])
    assert calculateFuel(100) == 150

    mocker.patch('builtins.input', side_effect=[1.5, 'y'])
    assert calculateFuel(100) == 152

def test_display():
    assert display(60, 120) == "\nRace will be 60 laps. You need 120 liters!"
    assert display(100, 150) == "\nRace will be 100 laps. You need 150 liters!"
    assert display(1, 2) == "\nRace will be 1 laps. You need 2 liters!"
