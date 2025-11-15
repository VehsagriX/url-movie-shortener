from typing import Annotated

from fastapi import Depends, APIRouter, status

from api.api_v1.short_urls_api.dependencies import (
    prefetch_short_url,
)
from api.api_v1.short_urls_api.crud import storage
from schemas.short_url import ShortUrl, ShortUrlCreate

router = APIRouter(
    prefix="/short-urs",
    tags=["Short URLs"],
)


@router.get(
    "/",
    response_model=list[ShortUrl],
)
def read_short_urls_list() -> list[ShortUrl]:
    return storage.get()


@router.post(
    "/",
    response_model=ShortUrl,
    status_code=status.HTTP_201_CREATED,
)
def create_short_url(short_url_create: ShortUrlCreate) -> ShortUrl:
    """При создании данных апи возвращает 201 статус код!!!"""
    return storage.create(short_url_create)


@router.get("/{slug}/", response_model=ShortUrl)
def get_short_url_by_slug(
    url: Annotated[
        ShortUrl,
        Depends(prefetch_short_url),
    ],
) -> ShortUrl:
    return url


@router.delete(
    "/{slug}/",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        # status.HTTP_204_NO_CONTENT: None,
        status.HTTP_404_NOT_FOUND: {
            "description": "URL not found",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "URL 'slug' not found",
                    }
                }
            },
        },
    },
)
def delete_short_url(
    url: Annotated[
        ShortUrl,
        Depends(prefetch_short_url),
    ],
) -> None:
    """При удалении данных апи возвращает 204 статус код!!!"""
    storage.delete(url)
