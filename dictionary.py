dic = {1: 'Joseph Akpan', 2: 'jau', 3: 'male'}
print(type(dic[3]))

# iteratikon for a dict
new_d = {'name': 'Joseph Akpan', 'age': 34, 'state': 'Akwa Ibom', 'status': 'Single'}

# to print only the key in the dictikonary
for x in new_d:
    print(x)

#print both the key and the value or either
for key, value in new_d.items():
    print(key, ' = ', value)

new_d['sibling']= 3
new_d['naughty']= 'jaspas'
print(new_d)

#delete an item in dictionatry
del new_d['naughty']
print(new_d)