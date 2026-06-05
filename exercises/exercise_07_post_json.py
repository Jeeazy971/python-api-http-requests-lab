import requests

url = "https://dummyjson.com/products/add"

headers = {
    "Accept": "application/json",
    "User-Agent": "python-api-http-requests-lab/1.0"
}

payload = {
    "title": "Developer Desk Lamp",
    "price": 29.99,
    "category": "home-decoration",
    "stock": 15
}

response = requests.post(url, headers=headers, json=payload, timeout=5)
status_code = response.status_code
content_type = response.headers.get("Content-Type")
accept = headers["Accept"]
user_agent = headers["User-Agent"]
response_data = response.json()

print("Product creation with POST")
print()
print(f"URL: {url}")
print(f"Status code: {status_code}")
print(f"Content-Type: {content_type}")
print()
print("Request headers sent:")
print(f"Accept: {accept}")
print(f"User-Agent: {user_agent}")
print()
print("Payload sent:")
print(f"Title: {payload['title']}")
print(f"Price: {payload['price']}")
print(f"Category: {payload['category']}")
print(f"Stock: {payload['stock']}")
print()
print("Response data:")
print(f"Created product ID: {response_data['id']}")
print(f"Title: {response_data['title']}")
print(f"Price: {response_data['price']}")
print(f"Category: {response_data['category']}")
print(f"Stock: {response_data['stock']}")
