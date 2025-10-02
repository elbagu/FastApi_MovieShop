from typing import Type, List
from src.base.service_base import ServiceBase
from src.models.responses.base.response import T, Response
from src.models.requests.movie.movie_model import MovieRequestCreate, MovieRequestUpdate


class MovieService(ServiceBase):
    def __init__(self):
        super().__init__("movies")

    def get_movies(
        self, response_type: Type[T], config: dict | None = None
    ) -> Response[T]:
        config = config or self.default_config
        return self.get(
            f"{self.url}",
            config=config,
            response_model=response_type,
        )


    def get_movie_by_id(self, movie_id: int, response_type: Type[T], config: dict | None = None) -> Response[T]:
        config = config or self.default_config
        return self.get(f"{self.url}/{movie_id}", config=config, response_model=response_type)

    def create_movie(self, movie: MovieRequestCreate, response_type: Type[T], config: dict | None = None) -> Response[T]:
        config = config or self.default_config
        return self.post(self.url, movie, config=config, response_model=response_type)

    def update_movie(self, movie_id: int, movie: MovieRequestCreate, response_type: Type[T], config: dict | None = None) -> Response[T]:
        config = config or self.default_config
        return self.put(f"{self.url}/{movie_id}", movie, config=config, response_model=response_type)

  
    def delete_movie(self, movie_id: int, response_type: Type[T] | None = None, config: dict | None = None) -> Response[T]:
        config = config or self.default_config
        return self.delete(f"{self.url}/{movie_id}", config=config, response_model=response_type)