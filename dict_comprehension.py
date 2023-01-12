# # ur = {x: x * 2 for x in range(4)}
# # # print('Using range(): ', ur)

# # # Lists
# # months = ["Jan", "Feb", "Mar", "Apr", "May", "June",
# #           "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
# # number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# # # Using one input list
# # numdict = {x: x**2 for x in number}
# # print("Using one input list to create dict: ", numdict)

# # # Using two input lists
# # months_dict = {key: value for (key, value) in zip(number, months)}
# # # print("Using two lists: ", months_dict)
# list = [12, 14, 16]
# mx = {x for x in range(10, 20)}
# # set_a = {mx if x not in list}
# # print(set_a)

# print(type(mx))

data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
gen_obj = (x for x in data)

# print(gen_obj)
# print(type(gen_obj))

for items in gen_obj:
    print(items, end=" ")
