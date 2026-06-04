import requests

url = "https://dummyjson.com/products"
params = {
    "limit": 5,
    "skip": 0
}

response = requests.get(url, params=params, timeout=5)
data = response.json()
products = data["products"]

total_products = data["total"]
limit = data["limit"]
skip = data["skip"]
number_of_products_received = len(products)

print("Products API with query params")
print()
print(f"Base URL: {url}")
print(f"Final URL: {response.url}")
print(f"Status code: {response.status_code}")
print()
print("Pagination:")
print(f"Total products: {total_products}")
print(f"Limit: {limit}")
print(f"Skip: {skip}")
print(f"Number of products received: {number_of_products_received}")
print()
print("First product:")
print(f"Title: {products[0]['title']}")
print(f"Category: {products[0]['category']}")
print(f"Price: {products[0]['price']}")
