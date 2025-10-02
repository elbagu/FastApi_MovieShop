import pytest
from typing import List
from src.models.services.movie_service import MovieService
from src.models.requests.movie.movie_model import MovieRequestCreate
from src.models.responses.movie.movie_response import MovieResponse

@pytest.fixture
def movie_service():
    return MovieService()

def test_create_and_get_movie(movie_service):
   
    created = movie_service.create_movie(
        MovieRequestCreate(
            name="Temp",
            director="X",
            gender=["Drama"],
            shop=1,
            rent=False
        ),
        response_type=MovieResponse
    )
    assert created.status in (200, 201)
    movie_id = created.data.id  

    movies_list = movie_service.get_movies(response_type=List[MovieResponse])
    assert movies_list.status == 200
    assert isinstance(movies_list.data, list)
    assert any(m.id == movie_id for m in movies_list.data)  

    resp = movie_service.get_movie_by_id(movie_id, response_type=MovieResponse)
    assert resp.status == 200
    
    movie_from_list = next((m for m in movies_list.data if m.id == movie_id), None)
    assert movie_from_list is not None

    assert resp.data.id == movie_from_list.id
    assert resp.data.name == movie_from_list.name
    assert resp.data.director == movie_from_list.director
    assert resp.data.gender == movie_from_list.gender
    assert resp.data.shop == movie_from_list.shop
    assert resp.data.rent == movie_from_list.rent

def test_get_movies_by_id_non_existent(movie_service):
    resp = movie_service.get_movie_by_id(9999, response_type=None)
    assert resp.status == 404