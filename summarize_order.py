def summarize_order(order):


""" Summarizes the order
    [IMPLEMENT ME]        1. Calculate the total (subtotal + tax) and store it in a variable named total (rounded to two decimals)        2. Store only the names of all the items in the order in a list called names        3. Return names and total.
    Args:        order: list of dicts that contain an item name and price
    Returns:        tuple of names and total. The return statement should look like 
        return names, total
    """

print_order(order)    # WRITE SOLUTION HERE

subtotal = calculate_subtotal(order)

tax = calculate_tax(subtotal)

total = round((subtotal + tax), 2)

names = [item["name"] for item in order]

return names, total
raise NotImplementedError()
