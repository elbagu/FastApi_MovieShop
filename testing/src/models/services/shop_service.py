from typing import Type
from src.base.service_base import ServiceBase
from src.models.responses.base.response import T, Response
from src.models.requests.shop.shop_model import ShopRequestCreate, ShopRequestUpdate


class ShopService(ServiceBase):
    def __init__(self):
        super().__init__("shops")

    def add_shop(
        self, shop: ShopRequestCreate, response_type: Type[T], config: dict | None = None
    ) -> Response[T]:
        config = config or self.default_config
        return self.post(
            self.url,
            shop,
            config=config,
            response_model=response_type,
        )

    def get_shops(self, response_type: Type[T], config: dict | None = None) -> Response[T]:
        config = config or self.default_config
        return self.get(self.url, config=config, response_model=response_type)

   
    def get_shop_by_id(self, shop_id: int, response_type: Type[T], config: dict | None = None) -> Response[T]:
        config = config or self.default_config
        return self.get(f"{self.url}/{shop_id}", config=config, response_model=response_type)

   
    def update_shop(self, shop_id: int, shop: ShopRequestUpdate, response_type: Type[T], config: dict | None = None) -> Response[T]:
        config = config or self.default_config
        return self.put(f"{self.url}/{shop_id}", shop, config=config, response_model=response_type)

    def delete_shop(self, shop_id: int, response_type: Type[T] | None = None, config: dict | None = None) -> Response[T]:
        config = config or self.default_config
        return self.delete(f"{self.url}/{shop_id}", config=config, response_model=response_type)