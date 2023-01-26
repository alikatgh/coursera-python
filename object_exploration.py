class A:  # 1 Class definition of A
    def __init__(self, c):  # 1.1 constructor for `A`
        print("---------Inside class A----------")
        self.c = c
    print("Print inside A.")

    def alpha(self):  # 1.2 local method `alpha`
        c = self.c + 1
        return c


print(dir(A))
print("Instantiating A..")
a = A(1)  # 2 Instantiating object `a` over class `A`
print(a.alpha())  # 3 Calling method `alpha()` over object of class `A`


class B:  # 4 Class definition of `B`
    def __init__(self, a):  # 5 constructor for `B`
        print("---------Inside class B----------")
        self.a = a

    print(a.alpha())  # 5.1 Calling method `alpha()` over object of class `A`
    d = 5
    print(d)
    print(a)


print("Instantiating B..")
b = B(a)  # 5.2 Instantiating object `a` over class `B`
print(a)
