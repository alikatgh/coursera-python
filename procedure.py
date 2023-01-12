def sum(a, b):
    return a + b


def bill_total(bill):
    total = 0.00
    for k, v in bill.items():
        total += v
    return total


def calculate_tax(percent, bill_total):
    return round((percent * bill_total) / 100.0, 2)


print(calculate_tax(12, 943))

fb = {
    'juice': 2.99
}
