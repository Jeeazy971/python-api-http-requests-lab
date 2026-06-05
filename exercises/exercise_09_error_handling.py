import requests

url = "https://dummyjson.com/products/99999999"

headers = {
    "Accept": "application/json",
    "User-Agent": "python-api-http-requests-lab/1.0"
}

try:
    response = requests.get(url, headers=headers, timeout=5)

    print("API request with error handling")
    print()
    print(f"URL: {url}")
    print(f"Status code: {response.status_code}")
    print()

    if response.status_code == 200:
        data = response.json()
        title = data['title']
        print("Product found:")
        print(f"Title: {title}")
    elif response.status_code == 404:
        print("Product not found.")
    elif 500 <= response.status_code < 600:
        print("Server error.")
    else:
        print(f"Unexpected status code: {response.status_code}")

except ValueError:
    print("The response is not valid JSON.")
except requests.exceptions.Timeout:
    print("The request timed out.")
except requests.exceptions.ConnectionError:
    print("Could not connect to the API.")
except requests.exceptions.RequestException:
    print("An error occurred during the request.")
