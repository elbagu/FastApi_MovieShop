import pytest
from typing import List
from src.models.services.movie_service import MovieService
from src.models.requests.movie.movie_model import MovieRequestCreate
from src.models.responses.movie.movie_response import MovieResponse
from src.models.responses.base.error_response import ErrorResponse

@pytest.fixture
def movie_service():
    return MovieService()

@pytest.mark.smoke
def test_post_movies_create_ok(movie_service):
    payload = MovieRequestCreate(
        name="Inception",
        director="Nolan",
        gender=["Sci-Fi"],
        shop=1,
        rent=False
    )
    resp = movie_service.create_movie(payload, response_type=MovieResponse)
    assert resp.status == 201
    assert isinstance(resp.data, MovieResponse)
    assert resp.data.name == "Inception"
    assert isinstance(resp.data.id, int)

def test_post_movies_missing_name(movie_service):
    payload = {
        "director": "Nolan",
        "gender": ["Sci-Fi"],
        "shop": 1,
        "rent": False
    }
    resp = movie_service.post(
        movie_service.url,
        data=payload,
        response_model=ErrorResponse
    )
    assert resp.status == 422
    assert isinstance(resp.data, ErrorResponse)
    assert any("name" in d.lower() for d in resp.data.detail)