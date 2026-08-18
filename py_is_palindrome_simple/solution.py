#!/usr/bin/env python3


def is_palindrome(word: str) -> bool:
    return word == word[::-1]


if __name__ == "__main__":
    print(is_palindrome("racecar"))  # True
    print(is_palindrome("madam"))    # True
    print(is_palindrome("hello"))    # False
    print(is_palindrome("Ana"))      # False
    print(is_palindrome(""))         # True
