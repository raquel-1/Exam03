def hidenp(small: str, big: str) -> bool:
    i = 0
    small_len = len(small)
    for j in big:
        if i < small_len:
            if j == small[i]:
                i = i + 1
    result = (i == small_len)
    return result
