class House:
    nr = 5
    b = 5

    def ce(self):
        print(self.nr)
        pass


house = House()
print(house.ce())
house.nr = '7'
print(house.ce())
House.nr = 7
print(house.ce())
