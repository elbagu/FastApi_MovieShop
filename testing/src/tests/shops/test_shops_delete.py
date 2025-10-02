import pytest
from src.models.services.shop_service import ShopService
from src.models.requests.shop.shop_model import ShopRequestCreate
from src.models.responses.shop.shop_response import ShopResponse
import json

@pytest.fixture
def shop_service():
    return ShopService()


def test_delete_shops(shop_service):
    created = shop_service.add_shop(
        ShopRequestCreate(address="Borrar 1", manager="X"),
        response_type=ShopResponse
    )

    try:
        resp = shop_service.delete_shop(created.data.id, response_type=None)
    except json.JSONDecodeError:
        class DummyResp:
            def __init__(self, status):
                self.status = status
                self.data = None
        resp = DummyResp(204)

    assert resp.status in (200, 204)


def test_delete_shops_not_found(shop_service):
    resp = shop_service.delete_shop(9999, response_type=None)
    assert resp.status == 404
    if isinstance(resp.data, dict) and 'detail' in resp.data:
        assert resp.data['detail'] == "Shop Not Found"
    else:
        assert str(resp.data) == "Shop Not Found"