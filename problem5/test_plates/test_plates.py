from plates import is_valid


def test_length():
    assert is_valid("CS") == True
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False


def test_starting_letters():
    assert is_valid("CS50") == True
    assert is_valid("1S50") == False
    assert is_valid("C150") == False


def test_numbers():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("CS5A") == False


def test_characters():
    assert is_valid("CS50") == True
    assert is_valid("CS.50") == False
    assert is_valid("CS 50") == False