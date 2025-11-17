from typing import Annotated

from fastapi import APIRouter, Depends, status

from api.api_v1.movies_api.crud import movie_storage
from api.api_v1.movies_api.dependencies import prefetch_movie
from schemas.movie import Movie

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


@router.get(
    "/",
    response_model=Movie,
)
def get_movie_by_id(
    movie: Annotated[Movie, Depends(prefetch_movie)],
) -> Movie:
    return movie


@router.delete(
    "/",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_movie(
    movie: Annotated[Movie, Depends(prefetch_movie)],
) -> None:
    """При удалении описали дополнительную информацию в документации в responses.
    Статус код при удалении status.HTTP_204_NO_CONTENT!!!
    """

    movie_storage.delete_movie(movie)
