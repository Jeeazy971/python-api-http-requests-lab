import requests

url = "https://dummyjson.com/products/1"

response = requests.get(url, timeout=5)
data = response.json()
status = response.status_code
print("Product API JSON response")
print()
print(f"URL: {url}")
print(f"Status code: {status}")
print()
print("Raw response type:")
print(type(response.text))
print()
print("JSON data type:")
print(type(data))
print()
print("Product details:")
print(f"Title: {data['title']}")
print(f"Category: {data['category']}")
print(f"Price: {data['price']}")
print(f"Rating: {data['rating']}")
print(f"Stock: {data['stock']}")
