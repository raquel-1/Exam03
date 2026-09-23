def pattern_tracker(text: str) -> int:
	n = 0
	digits = "0123456789"
	length = len(text)
	if length == 0 or length == 1: return n
	i = 0
	while i < length - 1:
		if text[i] in digits and text[i+1] in digits and text[i] < text[i + 1]:
			n += 1
		i += 1
	return n

if __name__ == "__main__":
	print(pattern_tracker("123"))
	print(pattern_tracker("12a34"))
	print(pattern_tracker("987654321"))
	print(pattern_tracker("01234567"))
	print(pattern_tracker("abc"))
	print(pattern_tracker("1a2b3c4"))
	print(pattern_tracker("112233"))
