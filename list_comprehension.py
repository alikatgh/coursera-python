# list comprehension
data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

data = [x+3 for x in data]
new_data = [x*2 for x in data]
fourx = [x for x in new_data if x % 4 == 0]
fourxsub = [x-1 for x in new_data if x % 4 == 0]
nines = [x for x in range(100) if x % 9 == 0]

for x in range(len(data)):
    data[x] = data[x] + 3

print("Updating the list: ", data)
print("Creating new list: ", new_data)
print("Divisible by four", fourx)
print("Divisible by four minus one: ", fourxsub)
print("Nines: ", nines)

ex1 = [x-1 for x in new_data if x % 5 == 0]
