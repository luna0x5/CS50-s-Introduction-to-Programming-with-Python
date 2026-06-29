from twttr import shorten


def test_lowercase():
    assert shorten("twitter") == "twttr"
    assert shorten("apple") == "ppl"


def test_uppercase():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("APPLE") == "PPL"


def test_mixed_case():
    assert shorten("TwItTeR") == "TwtTR"


def test_numbers():
    assert shorten("CS50") == "CS50"
    assert shorten("12345") == "12345"


def test_punctuation():
    assert shorten("Hello, world!") == "Hll, wrld!"
    assert shorten("!?.,") == "!?.,"


def test_no_vowels():
    assert shorten("rhythm") == "rhythm"


def test_only_vowels():
    assert shorten("aeiouAEIOU") == ""


def test_empty_string():
    assert shorten("") == ""