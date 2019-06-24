"""
Requirements:
    at least 15 characters
    at least one character is a digit
    at least one character is a special symbol (?!@#$*)
    at least one character is uppercase
"""

def check_password_has_digit(password):
    digits = '1234567890'
    for digit in digits:
        if digit in password:
            return True  
    return False


def check_password_has_special_symbol(password):
    special_symbols = "?!@#$*"
    for symbol in special_symbols:
        if symbol in password:
            return True
    return False


def check_password_contains_upper(password):
    return password.lower() != password

def password_check(password):
    """
    Input
    password (str): desired password for user

    Returns
    boolean: If password meets security critera or not
    """
    password_length = len(password) >= 15
    has_digit = check_password_has_digit(password)
    has_symbol =  check_password_has_special_symbol(password)
    contains_one_upper = check_password_contains_upper(password)
    return password_length and has_digit and has_symbol and contains_one_upper
