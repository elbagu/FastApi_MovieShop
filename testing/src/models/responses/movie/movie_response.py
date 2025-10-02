from typing import List
from pydantic import BaseModel

class MovieResponse(BaseModel):
    id: int
    name: str
    director: str
    gender: List[str]
    shop: int
    rent: bool