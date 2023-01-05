list1 = [1,2,4,5]
list2 = [6,7,8,9]

count = 0

for x in list1: 
    count +=1
    print(x, end = " ")
    for y in list2:
        count +=1 
        print(y, end = " ")

for i in range(1):
    for j in range(10):
        print(0, end = " ")
    print()