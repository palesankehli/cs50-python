from bank import value

def test_null():
    assert value("hello") == 0
    assert value("Hello, World") == 0

def test_twenty():
    assert value("hi") == 20

def test_hundred():
    assert value("Greetings") == 100
    assert value("Bonjour") == 100
