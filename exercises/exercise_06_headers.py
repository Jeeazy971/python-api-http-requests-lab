import requests

url = "https://dummyjson.com/products/1"

headers = {
    "Accept": "application/json",
    "User-Agent": "python-api-http-requests-lab/1.0"
}

response = requests.get(url, headers=headers, timeout=5)

data = response.json()
status_code = response.status_code
content_type = response.headers.get("Content-Type")
url_final = response.url

product_title = data["title"]
product_category = data["category"]
product_price = data["price"]

print("Product API request with headers")
print()
print(f"URL: {url_final}")
print(f"Status Code: {status_code}")
print(f"Content-Type: {content_type}")
print()
print("Request headers sent:")
print(f"Accept: {headers['Accept']}")
print(f"User-Agent: {headers['User-Agent']}")
print()
print("Product details:")
print(f"Title: {product_title}")
print(f"Category: {product_category}")
print(f"Price: {product_price}")
