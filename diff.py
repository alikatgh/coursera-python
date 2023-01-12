import functools

list = [1, 2, 3, 4, 5]
# print(list)


def add_it(x, y):
    return (x + y)


sum = functools.reduce(add_it, list)
# print(sum)


def square(x): return x ** 2


def double(x): return x + x


# print(list(map(square, list)))
# print(list(map(double, list)))

sum2 = (functools.reduce(lambda x, y: x + y, list))
sum3 = (functools.reduce(lambda x, y: x * y, list))
sum4 = (functools.reduce(lambda x, y: x ** y, list))
sum5 = (functools.reduce(lambda x, y: x / y, list))
print(sum2, sum3, sum4, sum5)
