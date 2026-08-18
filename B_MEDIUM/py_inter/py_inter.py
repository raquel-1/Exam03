def inter(s1: str, s2: str) -> str:
    result = ""
    for i in s1:
        for j in s2:
            if i == j and j not in result:
                result = result + i
    return result
