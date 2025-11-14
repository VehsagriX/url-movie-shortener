from fastapi import HTTPException, status

from api.api_v1.movies_api.crud import movie_storage
from schemas.movie import Movie


def prefetch_movie(slug: str):
    movie: Movie | None = movie_storage.get_movie_by_slug(slug)

    if movie:
        return movie
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Movie {slug!r} not found",
    )
