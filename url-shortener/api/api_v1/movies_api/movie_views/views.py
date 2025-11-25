from fastapi import status, APIRouter

from api.api_v1.movies_api.crud import movie_storage
from schemas.movie import MovieCreate, MovieRead, Movie

router = APIRouter(
    prefix="/movies",
    tags=["Movies"],
)


@router.get(
    "/",
    response_model=list[MovieRead],
)
def read_movies() -> list[Movie]:
    return movie_storage.get()


@router.post(
    "/",
    response_model=MovieRead,
    status_code=status.HTTP_201_CREATED,
)
def create_movie(movie_create: MovieCreate) -> Movie:
    movie = movie_storage.create_movie(movie_create)
    return movie
