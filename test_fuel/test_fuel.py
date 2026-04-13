from fuel import convert
from fuel import gauge

def test_correct_input():
    assert convert("1/2") == 50
    assert convert("1/4") == 25
    assert convert("1/100") == 1

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_errors():
   assert convert("1/0") == ZeroDivisionError

