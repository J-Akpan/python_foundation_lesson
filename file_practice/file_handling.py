file = open('doc.txt', mode = 'r')
data = file.read()

print(data)
file.close

# altenative foemat that closes the file automatically  is show below
with open('text.txt', mode = 'r') as file:
    content = file.read()
    print(content)