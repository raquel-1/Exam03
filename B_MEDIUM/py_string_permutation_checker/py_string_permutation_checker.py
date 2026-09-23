def sort_word(word: str) -> list[str]:
	i = 0
	word_l = list(word)
	length = len(word_l)
	while i < length:
		j = 0
		while  j < length - i - 1:
			if word_l[j] > word_l[j + 1]:
				word_l[j], word_l[j + 1] = word_l[j + 1], word_l[j]
			j += 1
		i += 1
	return word_l

def string_permutation_checker(s1: str, s2: str) -> bool:
	l1= len(s1)
	l2 = len(s2)
	if l1 == l2 == 0: return True
	if l1 != l2: return False
	if s1 == s2: return True

	w1 = sort_word(s1)
	w2 = sort_word(s2)
	if w1 == w2 : return True
	else: return False

	

if __name__ == "__main__":
	print(string_permutation_checker("abc", "bca"))
	print(string_permutation_checker("abc", "def"))
	print(string_permutation_checker("listen", "silent"))
	print(string_permutation_checker("hello", "bello"))
	print(string_permutation_checker("", ""))
	print(string_permutation_checker("a", ""))
	print(string_permutation_checker("Abc", "abc"))
	print(string_permutation_checker("a gentleman","elegant man"))