import pytest
from typing import List
from src.models.services.shop_service import ShopService
from src.models.requests.shop.shop_model import ShopRequestCreate
from src.models.responses.shop.shop_response import ShopResponse


@pytest.fixture
def shop_service():
    return ShopService()

def test_get_shops_list(shop_service):
    resp = shop_service.get_shops(response_type=List[ShopResponse])
    assert resp.status == 200
    assert isinstance(resp.data, list)

def test_get_shops_by_id_exists(shop_service):
    
    created = shop_service.add_shop(
        ShopRequestCreate(address="Calle X 100", manager="Ana", movies=[]),
        response_type=ShopResponse
    )
    assert created.status in (200, 201)
    shop_id = created.data.id
    
    resp = shop_service.get_shop_by_id(shop_id, response_type=ShopResponse)
    assert resp.status == 200
    assert resp.data.id == shop_id
    assert resp.data.address == "Calle X 100"
    assert resp.data.manager == "Ana"
    assert resp.data.movies == [] 

def test_get_shops_by_id_non_existent(shop_service):
    resp = shop_service.get_shop_by_id(9999, response_type=None)
    assert resp.status == 404