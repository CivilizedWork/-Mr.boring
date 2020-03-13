def is_palindrome(str):
    if str==str[::-1]:
        return True
    return False

is_palindrome('banana')