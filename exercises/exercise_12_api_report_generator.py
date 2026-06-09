import requests
from pathlib import Path


def get_products(limit, skip):
    url = "https://dummyjson.com/products"

    params = {
        "limit": limit,
        "skip": skip
    }

    response = requests.get(url, params=params, timeout=5)
    if response.status_code == 200:
        return response.json()

    return None


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


def create_report(data, average_price, most_expensive_product, lowest_stock_product):
    products = data["products"]

    content = f"""API Products Report

Total product available: {data["total"]}
Products received: {len(products)}
Limit: {data["limit"]}
Skip: {data["skip"]}

Average price: {average_price:.2f}

Most expensive product:
Title: {most_expensive_product['title']}
Price: {most_expensive_product['price']}

Lowest stock product:
Title: {lowest_stock_product['title']}
Stock: {lowest_stock_product['stock']}

Products list:
"""

    for product in products:
        content += f"- {product['title']} | {product['category']} | {product['price']} | stock: {product['stock']}\n"

    return content


def save_report(report_content):
    report_folder = Path("data") / "output" / "reports"
    report_folder.mkdir(parents=True, exist_ok=True)
    api_products_report_file = report_folder / "api_products_report.txt"

    api_products_report_file.write_text(report_content, encoding="utf-8")
    return api_products_report_file


data = get_products(10, 0)

if data is not None:
    products = data["products"]

    average_price = calculate_average_price(products)
    most_expensive_product = find_most_expensive_product(products)
    lowest_stock_product = find_lowest_stock_product(products)

    report_content = create_report(
        data,
        average_price,
        most_expensive_product,
        lowest_stock_product
    )

    report_path = save_report(report_content)

    print("API products report generated:")
    print(report_path)
else:
    print("Could not generate report.")
