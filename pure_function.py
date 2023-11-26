v = [1,3,4]





#to make it a pure function
def add_item(lst, item):
    nl = lst.copy()
    nl.append(item)
    return nl

new_v = add_item(v, 4)
print(v)
print(new_v)