class A:
    def __init__(self, c):
        print("---------Inside Class A---------")
        self.c = c
    print("print inside A")

    def alpha(self):
        c = self.c +1
        return c

print(dir(A))
print("Instantiating A")
a = A(1)
print (a.alpha())


class B:
    def __init__(self, a):
        print("-------inside class B-----")
        self.a = a

    print(a.alpha())
    d = 5
    print(d)
    print(a)

print("instantiating class B")
b = B(a)
print(a)

