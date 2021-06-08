# https://py.checkio.org/en/mission/acceptable-password-v/
# Electronic station
# Acceptable Password V


# Taken from mission Acceptable Password IV

def is_acceptable_password(password: str) -> bool:
    return ((len(password) > 6 and any([c.isnumeric() for c in password]) and any(
        [c.isalpha() for c in password])) or len(password) > 9) and 'password' not in password.lower()


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('short54') == True
    assert is_acceptable_password('muchlonger') == True
    assert is_acceptable_password('ashort') == False
    assert is_acceptable_password('muchlonger5') == True
    assert is_acceptable_password('sh5') == False
    assert is_acceptable_password('1234567') == False
    assert is_acceptable_password('12345678910') == True
    assert is_acceptable_password('password12345') == False
    assert is_acceptable_password('PASSWORD12345') == False
    assert is_acceptable_password('pass1234word') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
