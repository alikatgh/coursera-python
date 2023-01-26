class A:
    a = 1

    def plus(b, z):
        return b + z

    pass


# class B(A):
#     b = 2
#     pass

class B:
    a = 2

    def plus(b, z):
        return b - z

    pass


class C(A, B):
    pass


c = C()
# print(c.a, c.a)

print(issubclass(A, C))
