# def find_factorial(n):
#     if n < 0:
#         return 0
#     else:
#         fact = 1
#         for i in range(1, n + 1):
#             fact = fact * i
#         return fact


# print(find_factorial(int(5)))


def find_fact(n):
    if n == 1:
        return 1
    else:
        return n * find_fact(n - 1)


print(find_fact)
