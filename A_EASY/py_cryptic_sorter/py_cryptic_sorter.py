#!/usr/bin/env python3

def count_vowels(s: str) -> int:
    return sum(1 for char in s.lower() if char in "aeiouáéíóúü")

def cryptic_sorter(strings: list[str]) -> list[str]:
    length = len(strings)
    i = 0
    while i < length:
        j = 0
        while j < length - i - 1:
            # lenght
            if len(strings[j]) > len(strings[j + 1]):
                strings[j], strings[j + 1] = strings[j + 1], strings[j]
            # ASCII
            elif (
                (len(strings[j]) == len(strings[j + 1]))
                and (strings[j].lower() > strings[j + 1].lower())
            ) or (
                (len(strings[j]) == len(strings[j + 1]))
                and (strings[j].lower() == strings[j + 1].lower())
                and strings[j] > strings[j + 1]
            ):
                # lower greater than upper that's why they swap
                strings[j], strings[j + 1] = strings[j + 1], strings[j]
            # vowels
            elif (
                (len(strings[j]) == len(strings[j + 1]))
                and (strings[j].lower() == strings[j + 1].lower())
                and count_vowels(strings[j]) > count_vowels(strings[j + 1])
            ):
                strings[j], strings[j + 1] = strings[j + 1], strings[j]
            j += 1
        i += 1

    return strings

if __name__ == "__main__":
    print(cryptic_sorter(["apple","cat","banana","dog","elephant"]))
    print(cryptic_sorter(["aaa","bbb","AAA","BBB"]))
    print(cryptic_sorter(["hello","world","hi","test"]))
    print(cryptic_sorter([]))
    print(cryptic_sorter([""]))