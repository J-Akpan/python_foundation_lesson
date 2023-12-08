# clarification first
a = 'beans'
x = a*3
print(x +' ')

y = [1,3,4,5]
z = y*3
print(z)

# practice of class/objects

# class definition
class jayclass: 
    # 'pass' keyword is used when you want the code to run with nothnin in the class
    text = '*********I am really excited that i got here.***********'
    print('This is my first object in python')

    # this is a method.
    def hello(self):
        print('@@@@@Hello brother@@@@@')

# creating and initializing new instance
myclass = jayclass() 

#attribute referencing
print(jayclass.text)

# instance referencing
print(myclass.text)

#calling the method use the instance
print(myclass.hello())
