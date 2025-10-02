import pytest
from src.models.services.movie_service import MovieService
from src.models.requests.movie.movie_model import MovieRequestCreate
from src.models.responses.movie.movie_response import MovieResponse

@pytest.fixture
def movie_service():
    return MovieService()

def test_delete_movies(movie_service):
    created = movie_service.create_movie(
        MovieRequestCreate(name="Temp", director="X", gender=["Drama"], shop=1, rent=False),
        response_type=MovieResponse
    )
    resp = movie_service.delete_movie(created.data.id, response_type=None)
    assert resp.status == 204

def test_delete_movies_missing_name(movie_service):
    resp = movie_service.delete_movie(9999, response_type=None)
    assert resp.status == 404