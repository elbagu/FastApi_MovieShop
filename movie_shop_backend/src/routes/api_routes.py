from fastapi import APIRouter, HTTPException, status
from typing import List, Dict, Optional

from src.constants import MOVIE_NOT_FOUND_MESSAGE, SHOP_NOT_FOUND_MESSAGE
from src.schemas.schemas import Movie, MovieRequestCreate, MovieRequestUpdate, Shop, ShopRequestCreate, ChangeShopRequest

# In-memory "DB"
movies: Dict[int, Movie] = {}
shops: Dict[int, Shop] = {}
_next_movie_id = 1
_next_shop_id = 1

router = APIRouter()

# Obtener Movie por name, gender y/o director (no por Shop)
@router.get("/movies/search", response_model=List[Movie])
def search_movies(
    name: Optional[str] = None,
    gender: Optional[str] = None,
    director: Optional[str] = None
):
    result = list(movies.values())

    if name:
        result = [m for m in result if m.name.lower() == name.lower()]
    if gender:
        result = [m for m in result if gender in m.gender]
    if director:
        result = [m for m in result if m.director.lower() == director.lower()]

    return result

# Movies

@router.post("/movies", response_model=Movie, status_code=status.HTTP_201_CREATED)
def create_movie(movie_req: MovieRequestCreate):
    global _next_movie_id

    # Verificar que la shop exista
    if movie_req.shop not in shops:
        raise HTTPException(status_code=404, detail=SHOP_NOT_FOUND_MESSAGE)

    # Crear Movie 
    movie = Movie(
        id=_next_movie_id,
        name=movie_req.name,
        director=movie_req.director,
        gender=movie_req.gender,
        shop=movie_req.shop,
        rent=False
    )

    movies[_next_movie_id] = movie
    shops[movie.shop].movies.append(movie)
    _next_movie_id += 1

    return movie


@router.get("/movies", response_model=List[Movie])
def list_movies():
    return list(movies.values())


@router.get("/movies/{movie_id}", response_model=Movie)
def get_movie(movie_id: int):
    if movie_id not in movies:
        raise HTTPException(status_code=404, detail=MOVIE_NOT_FOUND_MESSAGE)
    return movies[movie_id]


@router.put("/movies/{movie_id}", response_model=Movie)
def update_movie(movie_id: int, movie_req: MovieRequestUpdate):
    if movie_id not in movies:
        raise HTTPException(status_code=404, detail=MOVIE_NOT_FOUND_MESSAGE)

    movie = movies[movie_id]
    movie.name = movie_req.name
    movie.director = movie_req.director
    movie.gender = movie_req.gender 
    return movie


@router.delete("/movies/{movie_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_movie(movie_id: int):
    if movie_id not in movies:
        raise HTTPException(status_code=404, detail=MOVIE_NOT_FOUND_MESSAGE)

    movie = movies.pop(movie_id)

    # Eliminar de la lista en la shop
    shop = shops[movie.shop_id]
    shop.movies.remove(movie)


# Shops


@router.post("/shops", response_model=Shop, status_code=status.HTTP_201_CREATED)
def create_shop(shop_req: ShopRequestCreate):
    global _next_shop_id

    shop = Shop(
        id=_next_shop_id,
        address=shop_req.address,
        manager=shop_req.manager,
        movies=[]
    )

    shops[_next_shop_id] = shop
    _next_shop_id += 1
    return shop


@router.get("/shops", response_model=List[Shop])
def list_shops():
    return list(shops.values())


@router.get("/shops/{shop_id}", response_model=Shop)
def get_shop(shop_id: int):
    if shop_id not in shops:
        raise HTTPException(status_code=404, detail=SHOP_NOT_FOUND_MESSAGE)
    return shops[shop_id]


@router.put("/shops/{shop_id}", response_model=Shop)
def update_shop(shop_id: int, shop_req: ShopRequestCreate):
    #uso ShopRequestCreate y no update por que me tira error?
    if shop_id not in shops:
        raise HTTPException(status_code=404, detail=SHOP_NOT_FOUND_MESSAGE)
    shops[shop_id].address = shop_req.address
    shops[shop_id].manager = shop_req.manager

  
    return shops[shop_id]


@router.delete("/shops/{shop_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_shop(shop_id: int):
    if shop_id not in shops:
        raise HTTPException(status_code=404, detail=SHOP_NOT_FOUND_MESSAGE)

    # Eliminar todas las movies asociadas
    shop = shops.pop(shop_id)
    for movie in list(movies.values()):
        if movie.shop == shop_id:
            movies.pop(movie.id, None)


# Consultar todas las Movie por Shop
@router.get("/shops/{shop_id}/movies", response_model=List[Movie])
def get_movies_by_shop(shop_id: int):
    if shop_id not in shops:
        raise HTTPException(status_code=404, detail=SHOP_NOT_FOUND_MESSAGE)
    return shops[shop_id].movies


# Consultar todas las Movie disponibles por Shop
@router.get("/shops/{shop_id}/movies/available", response_model=List[Movie])
def get_available_movies_by_shop(shop_id: int):
    if shop_id not in shops:
        raise HTTPException(status_code=404, detail=SHOP_NOT_FOUND_MESSAGE)
    return [m for m in shops[shop_id].movies if not m.rent]


# Cambiar de Shop una Movie
@router.patch("/movies/{movie_id}/change-shop", response_model=Movie)
def change_movie_shop(movie_id: int, req: ChangeShopRequest):
    if movie_id not in movies:
        raise HTTPException(status_code=404, detail=MOVIE_NOT_FOUND_MESSAGE)
    if req.new_shop_id not in shops:
        raise HTTPException(status_code=404, detail=SHOP_NOT_FOUND_MESSAGE)

    movie = movies[movie_id]

    # Quitar de la shop actual
    shops[movie.shop].movies = [m for m in shops[movie.shop].movies if m.id != movie_id]

    # Cambiar shop y agregar a la nueva
    movie.shop = req.new_shop_id
    shops[req.new_shop_id].movies.append(movie)

    return movie


