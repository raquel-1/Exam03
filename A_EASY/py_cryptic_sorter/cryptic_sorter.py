#!/usr/bin/env python3

def cryptic_sorter(strings: list[str]) -> list[str]:
    n = len(strings)
    i = 0
    while i < n:
        j = 0
        while j < n - i - 1:
            # lenght
            if len(n[j]) > len(n[j + 1]):
                strings[j], strings[j + 1] = strings[j + 1], strings[j]
            # ASCII
            elif n[j].lower() > n[j + 1].lower():
                strings[j], strings[j + 1] = strings[j + 1], strings[j]
            j += 1
    i += 1

    return strings

if __name__ == "__main__":
    print()