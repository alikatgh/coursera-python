def sr(str):
    if len(str) == 0:
        return str
    else:
        return sr(str[1:]) + str[0]


str = 'hello'
hello = sr(str)
print(hello)

data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

# Ex1: List comprehension: updating the same list
data = [x+3 for x in data]
new_data = [x*2 for x in data]
fourx = [x for x in new_data if x % 4 == 0]
fourxsub = [x-1 for x in new_data if x % 4 == 0]
nines = [x for x in range(100) if x % 9 == 0]

print("Updating the list: ", data)
print("Creating new list: ", new_data)
print("Divisible by four", fourx)
print("Divisible by four minus one: ", fourxsub)
print("Nines: ", nines)
