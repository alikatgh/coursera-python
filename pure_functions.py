my_list = [1, 2, 3]


def add_to_list(lst, item):
    new_local_list = lst.copy()
    new_local_list.append(item)
    return new_local_list


for x in range(4, 10):
    print(x)

new_list = add_to_list(my_list, x)

print(my_list)
print(new_list)
