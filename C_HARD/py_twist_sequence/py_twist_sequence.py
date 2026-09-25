def twist_sequence(arr: list[int], k: int) -> list[int]:
	if len(arr) == 0: return []
	i = 0
	while i < k:
		last = arr[-1]
		my_pop = arr[:len(arr) - 1]
		arr = [last] + my_pop
		i += 1
	return arr
		

if __name__ == "__main__":
	print(twist_sequence([1,2,3,4,5], 2))
	print(twist_sequence([1,2,3], 1))
	print(twist_sequence([1,2,3,4], 0))
	print(twist_sequence([1,2,3], 5))
	print(twist_sequence([], 3))
