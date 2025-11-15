from typing import Annotated

from fastapi import Depends, APIRouter, status

from api.api_v1.movies_api.crud import movie_storage
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
    return movie_storage.get()


@router.post(
    "/",
    response_model=Movie,
    status_code=status.HTTP_201_CREATED,
)
def create_movie(movie_create: MovieCreate):
    movie = movie_storage.create_movie(movie_create)
    return movie


@router.get(
    "/{slug}/",
    response_model=Movie,
)
def get_movie_by_id(
    movie: Annotated[Movie, Depends(prefetch_movie)],
) -> Movie:
    return movie


@router.delete(
    "/{slug}/",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "Movie not found",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Movie by 'slug' not found",
                    }
                }
            },
        }
    },
)
def delete_movie(
    movie: Annotated[Movie, Depends(prefetch_movie)],
) -> None:
    """При удалении описали дополнительную информацию в документации в responses.
    Статус код при удалении status.HTTP_204_NO_CONTENT!!!
    """

    movie_storage.delete_movie(movie)
