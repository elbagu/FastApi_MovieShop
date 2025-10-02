from typing import List, Optional
from pydantic import BaseModel


class MovieRequestCreate(BaseModel):
    name: str
    director: str
    gender: List[str]
    shop: int


class MovieRequestUpdate(BaseModel):
    name: Optional[str] = None
    director: Optional[str] = None
    gender: Optional[List[str]] = None
    