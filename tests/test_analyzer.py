import pytest

from api_client_lab.analyzer import calculate_average_price, find_lowest_stock_product, find_most_expensive_product


PRODUCTS = [
    {
        "id": 1,
        "title": "Keyboard",
        "category": "electronics",
        "price": 50,
        "stock": 12,
    },
    {
        "id": 2,
        "title": "Mouse",
        "category": "electronics",
        "price": 20,
        "stock": 30,
    },
    {
        "id": 3,
        "title": "Monitor",
        "category": "electronics",
        "price": 200,
        "stock": 5,
    },
]


def test_calculate_average_price_returns_average_product_price():
    result = calculate_average_price(PRODUCTS)
    
    assert result == pytest.approx(90.0)


def test_find_most_expensive_product_returns_product_with_highest_price():
    result = find_most_expensive_product(PRODUCTS)
    
    assert result == PRODUCTS[2]
    
    
def test_find_lowest_stock_product_returns_product_with_smallest_stock():
    result = find_lowest_stock_product(PRODUCTS)
    
    assert result == PRODUCTS[2]