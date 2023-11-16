# ctrating a single line 

with open('newfile.txt', 'w') as file:
    file.write('This lesson is quite awsome')

#creating multiple line of file
with open('multiline.txt', 'w') as content:
    content.writelines(['\n Agbo lives i a town of lagun which is not far from Ibadan',
    '\n He is in primary 5', 
    '\n He loves playing football always'])

# using try and except  to track error
try:
    with open('poem.txt', 'a') as poem:
        poem.writelines(['\n A little sleep we crave'
        '\n The price of no rank we pay', 
        '\n so swift the pain we bear',
        '\n till our days wash out we face'])
except FileNotFoundError as e:
    print('Error', e)