from fastapi import status, APIRouter

from api.api_v1.movies_api.crud import movie_storage
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
    return movie_storage.get()


@router.post(
    "/",
    response_model=Movie,
    status_code=status.HTTP_201_CREATED,
)
def create_movie(movie_create: MovieCreate):
    movie = movie_storage.create_movie(movie_create)
    return movie
