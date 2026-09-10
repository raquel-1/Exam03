def hidenp(small: str, big: str) -> bool:
    small_size = len(small)
    if small_size > len(big): return False
    if small_size == 0: return True
    i_small = 0
    for b in big:
        if b == small[i_small]:
            i_small += 1
            if i_small == small_size: return True
    return False

if __name__ == "__main__":
    print(hidenp("abc", "a1b2c3"))
    print(hidenp("ace", "abcde"))
    print(hidenp("aec", "abcde"))
    print(hidenp("", "abc"))
    print(hidenp("abc", "ab"))
    print(hidenp("aaaa", "aaa"))
    print(hidenp("sing","subsequence testing"))
