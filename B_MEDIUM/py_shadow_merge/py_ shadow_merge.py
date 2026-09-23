def sorted(list1: list[int]):
	length = len(list1)
	i = 0
	while i < length:
		j = 0
		while j < length - i - 1:
			if list1[j] > list1[j + 1]:
				list1[j], list1[j + 1] = list1[j + 1], list1[j]
			j += 1
		i += 1
	return list1


def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:
	copy = []
	copy += list1
	copy += list2
	return sorted(copy)

if __name__ == "__main__":
	print(shadow_merge([1,3,5], [2,4,6]))
	print(shadow_merge([1,2,3], [4,5,6]))
	print(shadow_merge([1], [2,3,4]))
	print(shadow_merge([], [1,2,3]))
	print(shadow_merge([1,1,2], [1,3,3]))