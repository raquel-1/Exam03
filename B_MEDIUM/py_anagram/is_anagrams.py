def is_anagrams(s1: str, s2: str) -> bool:
    return (sorted(s1) == sorted(s2))


if __name__ == "__main__":
    print(is_anagrams("racecar", "carraace"))
