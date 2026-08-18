#!/usr/bin/env python3


def is_palindrome(text: str) -> bool:
    cleaned = "".join(text.lower().split())
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    print(is_palindrome("racecar"))                      # True
    print(is_palindrome("A man a plan a canal Panama"))  # True
    print(is_palindrome("Was it a car or a cat I saw"))  # True
    print(is_palindrome("Never odd or even"))            # True
    print(is_palindrome("hello"))                        # False
    print(is_palindrome(""))                             # True
