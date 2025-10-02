from typing import Optional
from pydantic import BaseModel


class ShopRequestCreate(BaseModel):
    address: str
    manager: str

class ShopRequestUpdate(BaseModel):
    address: Optional[str] = None
    manager: Optional[str] = None