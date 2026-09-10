def sort_str(word_s: str) -> str:
    word = list(word_s)
    i = 0
    length = len(word)
    while i < length:
        j = 0
        while j < length - i - 1:
            if word[j] > word[j + 1]:
                word[j], word[j + 1] = word[j + 1], word[j]
            j += 1
        i += 1
    word_s = "".join(word)
    return word_s


def anagram(s1: str, s2: str) -> bool:
    clean_s1 = s1.lower().replace(" ", "")
    clean_s2 = s2.lower().replace(" ", "")

    if len(clean_s1) != len(clean_s2): return False

    return sort_str(clean_s1) == sort_str(clean_s2)


if __name__ == "__main__":
    print(anagram("listen", "silent"))
    print(anagram("Triangle", "Integral"))
    print(anagram("Dormitory", "Dirty Room"))
    print(anagram("hello", "world"))
    print(anagram("", ""))
    print(anagram("abc", "abcc"))
