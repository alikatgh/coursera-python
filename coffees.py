coffees = ['Espresso', 'Latte', 'Cappuccino',
           'Macchiato', 'Americano', 'Decaf']


def reverse(str):
    return str[3:0:-1]


reversed_coffees = map(reverse, coffees)
for x in reversed_coffees:
    print(x)
