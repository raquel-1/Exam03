def inter(s1: str, s2: str) -> str:
    result = ""
    for i in s1:
        for j in s2:
            if i == j and i not in result:
                result +=  i 
    return result

if __name__ == "__main__":
    print(inter("hello", "world"))
    print(inter("banana", "band"))
    print(inter("abcabc", "bc"))
    print(inter("abc", "xyz"))
    print(inter("", "abc"))