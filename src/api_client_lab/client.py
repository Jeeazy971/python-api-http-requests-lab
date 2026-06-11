import requests


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
