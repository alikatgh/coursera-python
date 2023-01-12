numbers = [15, 30, 47, 82, 95]


def lesser(numbers):
    return numbers < 50


small = list(map(lesser, numbers))
print(small)
