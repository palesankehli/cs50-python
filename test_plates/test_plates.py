from plates import is_valid

def test_length():
    assert is_valid("AA") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False

def test_start_letters():
    assert is_valid("AA") == True
    assert is_valid("A1") == False
    assert is_valid("12") == False
    assert is_valid("1A") == False

def test_numbers():
    assert is_valid("AAA222") == True
    assert is_valid("AAA022") == False
    assert is_valid("AAA22A") == False

def test_punctuation():
    assert is_valid("AA.10") == False
    assert is_valid("AA 10") == False
