from typing import Annotated

from fastapi import APIRouter, Depends, status

from api.api_v1.movies_api.crud import movie_storage
from api.api_v1.movies_api.dependencies import prefetch_movie
from schemas.movie import Movie, MovieUpdate, MovieUpdatePartial, MovieRead

router = APIRouter(
    prefix="/{slug}",
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

MovieBySlug = Annotated[Movie, Depends(prefetch_movie)]


@router.get(
    "/",
    response_model=MovieRead,
)
def get_movie_by_id(
    movie: MovieBySlug,
) -> Movie:
    return movie


@router.delete(
    "/",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_movie(
    movie: MovieBySlug,
) -> None:
    """При удалении описали дополнительную информацию в документации в responses.
    Статус код при удалении status.HTTP_204_NO_CONTENT!!!
    """

    movie_storage.delete_movie(movie)


@router.put("/", response_model=MovieRead)
def update_movie_by_slug(
    movie: MovieBySlug,
    movie_in: MovieUpdate,
) -> Movie:
    return movie_storage.update(movie, movie_in)


@router.patch("/", response_model=MovieRead)
def update_movie_by_slug_partial(
    movie: MovieBySlug,
    movie_in: MovieUpdatePartial,
) -> Movie:
    return movie_storage.update_partial(movie=movie, movie_in=movie_in)
