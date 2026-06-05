import requests

timeout = 5
get_url = "https://dummyjson.com/products/1"
post_url = "https://dummyjson.com/products/add"

headers = {
    "Accept": "application/json",
    "User-Agent": "python-api-http-requests-lab/1.0"
}

payload = {
    "title": "Timeout Safe Backpack",
    "price": 39.99,
    "category": "travel",
    "stock": 25
}

get_response = requests.get(get_url, headers=headers, timeout=timeout)
data = get_response.json()

post_request = requests.post(
    post_url, headers=headers, json=payload, timeout=timeout)
response_data = post_request.json()

print("Timeout practice with GET and POST")
print()
print("GET request:")
print(f"URL: {get_url}")
print(f"Status code: {get_response.status_code}")
print(f"Product title: {data['title']}")
print()
print("POST request:")
print(f"URL: {post_url}")
print(f"Status code: {post_request.status_code}")
print(f"Created product ID: {response_data['id']}")
print(f"Created product title: {response_data['title']}")
print()
print(f"Timeout used: {timeout} seconds")
