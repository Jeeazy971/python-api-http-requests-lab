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
