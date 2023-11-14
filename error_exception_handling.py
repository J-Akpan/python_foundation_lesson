# Eexeption handling handling errors in a more user friendly way usin 'try' and 'except'

def divide_by(a, b):
    return a/b
try:
    ans = divide_by(60, 0)

# adding base class exception
except Exception as e:
    print('something went wrong', e)
    print(e.__class__)

# Example2
def divide_by(a, b):
    return a/b
try:
    ans = divide_by(60, 0)

# adding base class exception to as well handle an unknown case of error
except ZeroDivisionError as e:
    print(e, ':we cant divide by zero')
except Exception as e:
    print(e, 'something went wrong')
