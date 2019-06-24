import sys
sys.path.append("../")
from password_check import password_check

def test_password_length_short():
    password = "thisismypasswd"
    expected = password_check(password)
    actual = False
    assert actual==expected, f"Password length incorrect, actual={actual}, expected={expected}"


def test_password_not_contains_one_digit():
    password = "thisismypassword"
    expected = password_check(password)
    actual = False
    message = f"""Password format incorrect, does not contain digit, actual={actual}, expected={expected}"""
    assert expected == actual, message


def test_password_not_contains_spc_chrtr():
    password = "thisismypassword"
    expected = password_check(password)
    actual = False
    message = f"""Password format incorrect, does not contain special character, actual={actual}, expected={expected}"""
    assert expected == actual, message


def test_password_not_contains_one_upper():
    password = "thisismypassword"
    expected = password_check(password)
    actual = False
    message = f"""Password format incorrect, does not contain upper, actual={actual}, expected={expected}"""
    assert expected == actual, message


def test_password_length_correct():
    password = "Th1s1smyPa$$word"
    expected = password_check(password)
    actual = True
    assert actual == expected, f"Password is marked as incorrect, but is correct, actual={actual}, expected={expected}"
