class ExampleClass:

    def __new__(cls, value):
        print("Creating new instance")

        # Call the superclass constructor to create the instance
        instance = super(ExampleClass, cls).__new__(cls)
        return instance

    def __init__(self, value):
        print("Initialising instance")
        self.payload = value


exampleInstance = ExampleClass(10)
print(exampleInstance.payload)
