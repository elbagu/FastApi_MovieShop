from typing import List, Optional
from pydantic import BaseModel

class Movie(BaseModel):
    id: int
    name: str
    director: str
    gender: List[str]
    shop: int
    rent: bool
    
class ChangeShopRequest(BaseModel):
    new_shop_id: int
    
class MovieRequestCreate(BaseModel):
    name: str
    director: str 
    gender: List[str]  
    shop: int

class MovieRequestUpdate(BaseModel):
    name: Optional[str] = None
    director: Optional[str] = None
    gender: Optional[List[str]] = None

class Shop(BaseModel):
    id: int
    address: str
    manager: str
    movies: List[Movie]

class ShopRequestCreate(BaseModel):
    address: str
    manager: str

class ShopRequestUpdate(BaseModel):
    address: Optional[str] = None
    manager: Optional[str] = None