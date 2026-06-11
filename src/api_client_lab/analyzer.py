def calculate_average_price(products):
    if not products:
        return None

    total_products_price = 0

    for product in products:
        price = product["price"]
        total_products_price += price

    average_price = total_products_price / len(products)
    return average_price


def find_most_expensive_product(products):
    if not products:
        return None

    most_expensive_product = products[0]

    for product in products[1:]:
        if product["price"] > most_expensive_product["price"]:
            most_expensive_product = product

    return most_expensive_product


def find_lowest_stock_product(products):
    if not products:
        return None

    low_stock_product = products[0]

    for product in products[1:]:
        if product["stock"] < low_stock_product["stock"]:
            low_stock_product = product

    return low_stock_product
