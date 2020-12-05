#sets_intersection = lambda a, b: [num for num in sorted(list(set(a))) if num in sorted(b)]

def sets_intersection(a, b):
	return [num for num in sorted(set(a)) if num in b]

print(sets_intersection([1, 2, 3, 4, 5, 6, 7, 8], [10, 25, 52, 80, 1, 46, 6, 33, 14, 27, 19]))
print(sets_intersection([1, 1, 1], [2, 2, 2]))
print(sets_intersection([3, 2, 1], [4, 3, 2, 1]))
print(sets_intersection([1, 2, 3, 4, 5], [0, 2, 4, 6, 8, 10]))
print(sets_intersection([6, 7, 1, 2, 1, 3, 4, 5], [7, 8, 1, 3, 2, 1, 7, 3, 7, 10]))
