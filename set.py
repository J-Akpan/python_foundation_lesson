set_a = {2,4,6,8,9,4}

#how to print set
print(*set_a)

#add to a set
set_a.add(12)
print(*set_a)

#remove value from a set
set_a.pop()
print(*set_a)

set_a.pop()
print(*set_a)

# maths in sedt
first_set  = {2, 4, 5, 6, 7, 8, 9, 12, 3}
second_set = {3, 5, 7,11 ,66, 8}

# union of a set
print(first_set.union(second_set))
print(first_set | second_set)

#set intersection
print(first_set.intersection(second_set))
print(first_set & second_set)

#set difference
print(first_set.difference(second_set))
print (first_set - second_set)

#symetrical diference
print(first_set.symmetric_difference(second_set))
print(first_set ^ second_set)