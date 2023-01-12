def find_num(num):
    count = 0
    for x in range(100):
        if x == num:
            print("Total Iterations: " + str(count))
            return x
        count += 1


print(find_num(143))
