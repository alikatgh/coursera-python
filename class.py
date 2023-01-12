class superClass:
    a = 5
    print(a)

    def call_super_class(self):
        print("Hey, it's me, call_super_class!")


my_instance = superClass()
# print(superClass.a)

print(my_instance.call_super_class())

# class MyClass:
#     a = 5

#     def hello():
#         print("Hello, World!")


# myc = MyClass()
# print(myc.a)
# print(myc.hello())
