from jar import Jar
import pytest

def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5

def test_withdraw():
    jar = Jar(size = 8)
    jar.withdraw(7)
    assert jar.size == 1

def test_too_many_ate():
    jar = Jar(10, 5)
    with pytest.raises(ValueError):
        jar.withdraw(6)

def test_too_many_added():
    jar = Jar(10)
    with pytest.raises(ValueError):
        jar.deposit(12)

def test_wrong_capacity_value():
    with pytest.raises(ValueError):
        jar = Jar(capacity = -1)

def test_too_many_cookies():
    with pytest.raises(ValueError):
        jar = Jar(10, 20)
