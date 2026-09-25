#!/usr/bin/env python3

def bracket_validator(s: str) -> bool:
	
	if len(s) == 0: return True
	if len(s) == 1: return False

	collect = ""
	n = len(s)
	i = 0
	while i < n:
		if s[i] == "(" or s[i] == "{" or s[i] == "[":
			collect += s[i]
		elif s[i] == ")" or s[i] == "}" or s[i] == "]":
			if len(collect) == 0: return False
			last = collect[-1]
			if (s[i] == ")" and last == "(") or (s[i] == "}" and last == "{") or (s[i] == "]" and last == "["):
				# pop # hello -> hell
				new = collect[:-1]
				collect = new
			else: return False
		i += 1
	if len(collect) == 0: return True
	else: return False


if __name__ == "__main__":
	print(bracket_validator("()"))
	print(bracket_validator("()[]{}"))
	print(bracket_validator("(]"))
	print(bracket_validator("([)]"))
	print(bracket_validator("{[]}"))
	print(bracket_validator("hello(world)"))
	print(bracket_validator("((())"))
	print(bracket_validator(""))