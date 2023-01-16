menu = {
    1: {"name": 'espresso',
        "price": 1.99},
    2: {"name": 'coffee',
        "price": 2.50},
    3: {"name": 'cake',
        "price": 2.79},
    4: {"name": 'soup',
        "price": 4.50},
    5: {"name": 'sandwich',
        "price": 4.99}
}


def calculate_subtotal(order):
    order = [1, 2, 3, 4]
    subtotal = 0

    for item in order:
        subtotal += menu[item]['price']
    print(subtotal)

    sum = sum(item['price'] for item in menu.values())
    print(sum)

    raise NotImplementedError()


def calculate_tax(subtotal):
    subtotal = round(subtotal * 15 % 2)
    print('Calculating tax from subtotal...')

    raise NotImplementedError()


def summarize_order(order):
    total = round(calculate_subtotal, 2) + round(calculate_tax, 2)
    names = order[names] + total
    return names, total

    print_order(order)

    # WRITE SOLUTION HERE

    raise NotImplementedError()


def print_order(order):
    print('You have ordered ' + str(len(order)) + ' items')
    items = []
    items = [item["name"] for item in order]
    print(items)
    return order

# This function is provided for you, and will display the menu


def display_menu():
    print("------- Menu -------")
    for selection in menu:
        print(
            f"{selection}. {menu[selection]['name'] : <9} | {menu[selection]['price'] : >5}")
    print()

# This function is provided for you, and will create an order by prompting the user to select menu items


def take_order():
    display_menu()
    order = []
    count = 1
    for i in range(3):
        item = input('Select menu item number ' +
                     str(count) + ' (from 1 to 5): ')
        count += 1
        order.append(menu[int(item)])
    return order


def main():
    order = take_order()
    print_order(order)

    # subtotal = calculate_subtotal(order)
    # print("Subtotal for the order is: " + str(subtotal))

    # tax = calculate_tax(subtotal)
    # print("Tax for the order is: " + str(tax))

    # items, subtotal = summarize_order(order)


if __name__ == "__main__":
    main()
