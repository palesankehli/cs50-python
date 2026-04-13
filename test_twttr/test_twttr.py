
from twttr import shorten

def test_lowercase():
    assert shorten("twitter") == "twttr"
    assert shorten("happily") == "hpply"

def test_uppercase():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("PALESA") == "PLS"

def test_numbers():
    assert shorten("PALESA023") == "PLS023"
    assert shorten("CS50") == "CS50"

def test_punctuation():
    assert shorten("gmail.com") == "gml.cm"
    assert shorten("@nunu") == "@nn"
