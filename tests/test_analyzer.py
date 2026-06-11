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


SINGLE_PRODUCT = [
    {
        "id": 1,
        "title": "USB Cable",
        "category": "accessories",
        "price": 15,
        "stock": 8,
    }
]


def test_calculate_average_price_returns_product_price_when_there_is_one_product():
    result = calculate_average_price(SINGLE_PRODUCT)

    assert result == pytest.approx(15.0)


def test_find_most_expensive_product_returns_product_when_there_is_one_product():
    result = find_most_expensive_product(SINGLE_PRODUCT)

    assert result == SINGLE_PRODUCT[0]


def test_find_lowest_stock_product_returns_product_when_there_is_one_product():
    result = find_lowest_stock_product(SINGLE_PRODUCT)

    assert result == SINGLE_PRODUCT[0]


def test_calculate_average_price_returns_none_when_products_are_empty():
    result = calculate_average_price([])

    assert result is None


def test_find_most_expensive_product_returns_none_when_products_are_empty():
    result = find_most_expensive_product([])

    assert result is None


def test_find_lowest_stock_product_returns_none_when_products_are_empty():
    result = find_lowest_stock_product([])

    assert result is None
