import pytest
from src.models.services.movie_service import MovieService
from src.models.requests.movie.movie_model import MovieRequestUpdate, MovieRequestCreate
from src.models.responses.movie.movie_response import MovieResponse
from src.models.responses.base.error_response import ErrorResponse

@pytest.fixture
def movie_service():
    return MovieService()

def test_put_movies_updated_ok(movie_service):
 
    created = movie_service.create_movie(
        MovieRequestCreate(name="Inception", director="Nolan", gender=["Sci-Fi"], shop=1),
        response_type=MovieResponse
    )
    movie_id = created.data.id

    update = MovieRequestUpdate(name="Inception Updated", director="Nolan", gender=["Sci-Fi"], shop=1, rent=True)
    resp = movie_service.update_movie(movie_id, update, response_type=MovieResponse)
    assert resp.status == 200
    assert resp.data.name == "Inception Updated"
    
def test_put_movies_non_existent(movie_service):
    update = MovieRequestUpdate(
        name="random", director="random", gender=["random"]
    )
    resp = movie_service.update_movie(9999, update, response_type=None)

    assert resp.status == 404
    assert isinstance(resp.data, dict)
    assert "detail" in resp.data
    assert resp.data["detail"] == "Movie Not Found"