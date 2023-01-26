class Fruit():
    def __init__(self, fruit):
        print('Fruit type: ', fruit)


class Flavor(Fruit):
    def __init__(self):
        super().__init__('Apple')
        print('Apple is sweet!')


apple = Flavor()
