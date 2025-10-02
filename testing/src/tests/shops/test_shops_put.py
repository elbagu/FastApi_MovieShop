import pytest
from src.models.services.shop_service import ShopService
from src.models.requests.shop.shop_model import ShopRequestUpdate
from src.models.responses.shop.shop_response import ShopResponse


@pytest.fixture
def shop_service():
    return ShopService()

def test_put_shops_updated_ok(shop_service):
    created = shop_service.add_shop(
        ShopRequestUpdate(address="Calle A 1", manager="Old", movies=[]),
        response_type=ShopResponse
    )
    shop_id = created.data.id

    update = ShopRequestUpdate(address="Calle Falsa 123", manager="Frutillita", movies=[])
    resp = shop_service.update_shop(shop_id, update, response_type=ShopResponse)
    assert resp.status == 200
    assert resp.data.address == "Calle Falsa 123"
    assert resp.data.manager == "Frutillita"

def test_put_shops_non_existent(shop_service):
    update = ShopRequestUpdate(address="Random Street", manager="random", movies=[1,2,3])
    resp = shop_service.update_shop(9999, update, response_type=None)
    assert resp.status == 404