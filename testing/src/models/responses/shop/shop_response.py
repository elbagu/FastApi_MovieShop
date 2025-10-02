from typing import List
from typing import Optional

from pydantic import BaseModel
from src.models.responses.movie.movie_response import MovieResponse

class ShopResponse(BaseModel):
    id: int
    address: str
    manager: str
    movies: List[MovieResponse]


class EmptyResponse(BaseModel):
    data: Optional[dict] = None