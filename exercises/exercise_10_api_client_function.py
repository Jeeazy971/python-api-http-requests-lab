import requests


def get_product(product_id):
    url = f"https://dummyjson.com/products/{product_id}"

    headers = {
        "Accept": "application/json",
        "User-Agent": "python-api-http-requests-lab/1.0"
    }

    response = requests.get(url, headers=headers, timeout=5)

    if response.status_code == 200:
        return response.json()

    return None


product = get_product(1)

print("API client function practice")
print()
if product is not None:
    print("Product found:")
    print(f"Title: {product['title']}")
    print(f"Category: {product['category']}")
    print(f"Price: {product['price']}")
    print(f"Stock: {product['stock']}")
else:
    print("Product not found or request failed.")
