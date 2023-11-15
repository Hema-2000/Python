A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])

# copying a frozenset
C = A.copy()
print(C)

# union
union_set = A.union(B)
print(union_set)

# intersection
intersection_set = A.intersection(B)
print(intersection_set)

difference_set = A.difference(B)
print(difference_set)

# symmetric_difference
symmetric_difference_set = A.symmetric_difference(B)
print(symmetric_difference_set)

#append(),update,add() all these functions are not possible in frozenset
fruits = frozenset(["apple", "banana", "orange"])
print(fruits)#frozenset({'apple', 'banana', 'orange'})
fruits.append("pink")#AttributeError: 'frozenset' object has no attribute 'append'
print(fruits)
