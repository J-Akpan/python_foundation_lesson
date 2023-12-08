list1 = ["jay", 12, 34.3, "bind"]

# to print the items in the list
print(*list1)
print(list1, sep=" ")

# to add to the list method 1
list1.insert(len(list1), 6)
print(list1, sep=" ")

# method 2
list1.append('value')
print(*list1)

# method 3
list1.extend(['joseph', 342, 'Ima Ndo'])
print(*list1)

# remove from a list
list1.pop(1)
print(*list1)

#remove methos 2
del list1[0]
print(*list1)

# Iterating thro a list
for i in list1:
    print('list1 values are:', i)
