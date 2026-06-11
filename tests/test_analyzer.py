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

TWO_PRODUCTS = [
    {
        "id": 1,
        "title": "Notebook",
        "category": "office",
        "price": 10,
        "stock": 20,
    },
    {
        "id": 2,
        "title": "Desk Lamp",
        "category": "office",
        "price": 30,
        "stock": 7,
    },
]

SINGLE_PRODUCT = [
    {
        "id": 1,
        "title": "USB Cable",
        "category": "accessories",
        "price": 15,
        "stock": 8,
    }
]

PRODUCTS_WITH_MISSING_PRICE = [
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
        "stock": 30,
    },
]

PRODUCTS_WITH_MISSING_STOCK = [
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
    },
]

PRODUCTS_WITH_ZERO_PRICE = [
    {
        "id": 1,
        "title": "Free Sticker",
        "category": "accessories",
        "price": 0,
        "stock": 100,
    },
    {
        "id": 2,
        "title": "USB Hub",
        "category": "accessories",
        "price": 50,
        "stock": 15,
    },
]


@pytest.fixture
def sample_products():
    return [
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


@pytest.fixture
def single_sample_product():
    return [
        {
            "id": 1,
            "title": "USB Cable",
            "category": "accessories",
            "price": 15,
            "stock": 8,
        }
    ]


@pytest.fixture
def sample_products_with_missing_price():
    return [
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
            "stock": 30,
        },
    ]


@pytest.fixture
def sample_products_with_missing_stock():
    return PRODUCTS_WITH_MISSING_STOCK


@pytest.mark.parametrize(
    "products, expected_average",
    [
        (PRODUCTS, 90.0),
        (SINGLE_PRODUCT, 15.0),
        (TWO_PRODUCTS, 20.0),
        (PRODUCTS_WITH_ZERO_PRICE, 25.0),
    ],
)
def test_calculate_average_price_returns_expected_average(products, expected_average):
    result = calculate_average_price(products)

    assert result == pytest.approx(expected_average)


def test_find_most_expensive_product_returns_product_with_highest_price(sample_products):
    result = find_most_expensive_product(sample_products)

    assert result == sample_products[2]


def test_find_lowest_stock_product_returns_product_with_smallest_stock(sample_products):
    result = find_lowest_stock_product(sample_products)

    assert result == sample_products[2]


def test_find_most_expensive_product_returns_product_when_there_is_one_product(single_sample_product):
    result = find_most_expensive_product(single_sample_product)

    assert result == single_sample_product[0]


def test_find_lowest_stock_product_returns_product_when_there_is_one_product(single_sample_product):
    result = find_lowest_stock_product(single_sample_product)

    assert result == single_sample_product[0]


def test_calculate_average_price_returns_none_when_products_are_empty():
    result = calculate_average_price([])

    assert result is None


def test_find_most_expensive_product_returns_none_when_products_are_empty():
    result = find_most_expensive_product([])

    assert result is None


def test_find_lowest_stock_product_returns_none_when_products_are_empty():
    result = find_lowest_stock_product([])

    assert result is None


def test_calculate_average_price_raises_key_error_when_price_is_missing(sample_products_with_missing_price):
    with pytest.raises(KeyError):
        calculate_average_price(sample_products_with_missing_price)


def test_find_most_expensive_product_raises_key_error_when_price_is_missing(sample_products_with_missing_price):
    with pytest.raises(KeyError):
        find_most_expensive_product(sample_products_with_missing_price)


def test_find_lowest_stock_product_raises_key_error_when_stock_is_missing(sample_products_with_missing_stock):
    with pytest.raises(KeyError):
        find_lowest_stock_product(sample_products_with_missing_stock)
