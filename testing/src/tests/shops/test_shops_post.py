import pytest
from src.models.services.shop_service import ShopService
from src.models.requests.shop.shop_model import ShopRequestCreate
from src.models.responses.shop.shop_response import ShopResponse
from src.models.responses.base.error_response import ErrorResponse



@pytest.fixture
def shop_service():
    return ShopService()

@pytest.mark.smoke
def test_post_shops_create_ok(shop_service):
    payload = ShopRequestCreate(address="Av. A  123", manager="Pepito")
    resp = shop_service.add_shop(payload, response_type=ShopResponse)
    assert resp.status == 201
   

def test_post_shops_validation(shop_service):
    payload = ShopRequestCreate.model_construct(address="Av. A  123", movies=[])
    resp = shop_service.post(shop_service.url, data=payload, response_model=ErrorResponse)
    assert resp.status == 422
    assert isinstance(resp.data, ErrorResponse)
    assert "validation error" in resp.data.detail[0].lower()
