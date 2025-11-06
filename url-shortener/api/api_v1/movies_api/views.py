from typing import Annotated

from fastapi import Depends, APIRouter

from api.api_v1.movies_api.crud import MOVIES
from api.api_v1.movies_api.dependencies import prefetch_movie
from schemas.movie import Movie


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


@router.get(
    "/{movie-id}",
    response_model=Movie,
)
def get_movie_by_id(movie: Annotated[Movie, Depends(prefetch_movie)]) -> Movie:
    return movie
