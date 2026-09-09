#!/usr/bin/env python3

def bracket_validator(s: str) -> bool:
    data_dic= {
        "(": ")",
        "[": "]",
        "{": "}",
    }
    pila_open = [] # only ({[
    for char in s:
        # char in open
        if char in data_dic.keys():
            pila_open.append(char)
        # char in close
        elif char in data_dic.values():
            if len(pila_open) <= 0:
                return False
            elif char != data_dic[pila_open[-1]]:
                return False
            else:
                pila_open.pop()
    
    return len(pila_open) == 0


if __name__ == "__main__":
    print(bracket_validator("()"))
    print(bracket_validator("()[]{}"))
    print(bracket_validator("(]"))
    print(bracket_validator("([)]"))
    print(bracket_validator("{[]}"))
    print(bracket_validator("hello(world)"))
    print(bracket_validator("((())"))
    print(bracket_validator(""))
