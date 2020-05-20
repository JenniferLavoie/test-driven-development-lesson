"""
Requirements:
    at least 15 characters
    at least one character is a digit
    at least one character is a special symbol (?!@#$*)
    at least one character is uppercase
"""


def password_check(password):
    """
    Input
    password (str): desired password for user

    Returns
    boolean: If password meets security critera or not
    """
    if not check_password_length(password):
        return False
    return None
