#!/usr/bin/env python3


def valid_anagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


if __name__ == "__main__":
    print(valid_anagram("racecar", "carrace"))  # True
    print(valid_anagram("jar", "jam"))          # False
    print(valid_anagram("listen", "silent"))    # True
    print(valid_anagram("aabbcc", "abcabc"))    # True
    print(valid_anagram("abc", "ab"))           # False
    print(valid_anagram("", ""))               # True
