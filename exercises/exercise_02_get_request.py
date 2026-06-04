import requests

url = "https://api.github.com"

response = requests.get(url)

print("GitHub API request")
print()
print(f"URL: {response.url}")
print(f"Status code: {response.status_code}")
print()
print("Raw response:")
print(response.text)