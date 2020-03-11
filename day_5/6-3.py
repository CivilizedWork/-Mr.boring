def first(word):
    """Returns the first character of a string."""
    return word[0]


def last(word):
    """Returns the last of a string."""
    return word[-1]


def middle(word):
    """Returns all but the first and last characters of a string."""
    return word[1:-1]

print(middle(' '))
#两个字母 单字母 空字符情况什么都显示不出来
def is_palindrome(str):
    if len(str)<=1:
        return True

    if first(str) != last(str):
        return False
    return is_palindrome(middle(str))

print(is_palindrome('gay'))
print(is_palindrome('a'))
print(is_palindrome('noon'))
