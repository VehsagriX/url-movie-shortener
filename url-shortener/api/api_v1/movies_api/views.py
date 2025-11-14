from typing import Annotated

from fastapi import Depends, APIRouter, status

from api.api_v1.movies_api.crud import MOVIES
from api.api_v1.movies_api.dependencies import prefetch_movie
from schemas.movie import Movie, MovieCreate

router = APIRouter(
    prefix="/movies",
    tags=["Movies"],
)


@router.get(
    "/",
    response_model=list[Movie],
)
def read_movies():
    return MOVIES


@router.post(
    "/",
    response_model=Movie,
    status_code=status.HTTP_201_CREATED,
)
def create_movie(movie_create: MovieCreate):
    return Movie(**movie_create.model_dump())


@router.get(
    "/{slug}",
    response_model=Movie,
)
def get_movie_by_id(
    movie: Annotated[Movie, Depends(prefetch_movie)],
) -> Movie:
    return movie
