from api_client_lab.client import get_products
import api_client_lab.client as client_module


class FakeResponse:
    status_code = 200

    def json(self):
        return {
            "total": 2,
            "limit": 2,
            "skip": 0,
            "products": [
                {
                    "id": 1,
                    "title": "Keyboard",
                    "price": 50,
                    "stock": 12,
                },
                {
                    "id": 2,
                    "title": "Mouse",
                    "price": 20,
                    "stock": 30,
                },
            ],
        }


def test_get_products_returns_json_when_status_code_is_200(monkeypatch):
    def fake_get(url, params, timeout):
        return FakeResponse()

    monkeypatch.setattr(client_module.requests, "get", fake_get)

    result = get_products(2, 0)

    assert result["total"] == 2
    assert result["limit"] == 2
    assert result["skip"] == 0
    assert len(result["products"]) == 2
    assert result["products"][0]["title"] == "Keyboard"


class FakeErrorResponse:
    status_code = 500

    def json(self):
        return {}


def test_get_products_returns_none_when_status_code_is_not_200(monkeypatch):
    def fake_get(url, params, timeout):
        return FakeErrorResponse()

    monkeypatch.setattr(client_module.requests, "get", fake_get)

    result = get_products(2, 0)

    assert result is None
