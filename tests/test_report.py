from api_client_lab.report import create_report


data = {
    "total": 2,
    "limit": 2,
    "skip": 0,
    "products": [
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
    ],
}

average_price = 35.0
most_expensive_product = data["products"][0]
lowest_stock_product = data["products"][0]


def test_create_report_contains_expected_information():
    result = create_report(
        data,
        average_price,
        most_expensive_product,
        lowest_stock_product,
    )

    assert "API Products Report" in result
    assert "Total product available: 2" in result
    assert "Products received: 2" in result
    assert "Limit: 2" in result
    assert "Skip: 0" in result
    assert "Average price: 35.00" in result
    assert "Most expensive product:" in result
    assert "Title: Keyboard" in result
    assert "Price: 50" in result
    assert "Lowest stock product:" in result
    assert "Stock: 12" in result
    assert "- Keyboard | electronics | 50 | stock: 12" in result
    assert "- Mouse | electronics | 20 | stock: 30" in result
