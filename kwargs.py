# function that takes in a limited amount of arguments

def sum(a, b, c):
    return a + b + c

# this will only run withnout error if there are only 3 arguments 
print(sum(3, 4, 4))

# alternatively for args

def sum(*args):
    sum = 0
    for x in args:
        sum += x
    return sum
print(sum(1, 3.5, 3, 8, 33.1))

# kwargs example
def sum(**kwargs):
    sum = 0
    for k, v in kwargs.items():
        sum += v
    return round(sum, 2)
print(sum(rice = 45.54, beans = 47, garri = 2.22))

# usning k instead of v will give error bcos it will return the keys not the value
# i.e rice, beans, garri since they are strings, they cant be added up