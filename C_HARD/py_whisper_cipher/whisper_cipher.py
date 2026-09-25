
def my_find(a: str, abc:str) -> int:
    i = 0
    while i < len(abc) and abc[i] != a:
        i += 1
    return i

def whisper_cipher(text: str, shift: int) -> str:
    ma = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    mi = "abcdefghijklmnopqrstuvwxyz"
    copy = ""
    i = 0
    while i < len(text):
        if text[i] in ma or text[i] in mi:
            index = 0
            if text[i] in ma:
                index = my_find(text[i], ma)
            else:
                index = my_find(text[i], mi)
            new_pos =  (index + shift) % 26
            if text[i] in ma:
                copy += ma[new_pos]
            else:
                copy += mi[new_pos]
        i += 1
    return copy		


if __name__ == "__main__":
    print(whisper_cipher("hello", 3))
    print(whisper_cipher("Hello World!", 1))
    print(whisper_cipher("xyz", 3))
    print(whisper_cipher("hello", 3))
    print(whisper_cipher("ABC123def", 5))
    print(whisper_cipher("", 10))
    print(whisper_cipher("abc", -3))
