from typing import Annotated

from fastapi import APIRouter, Depends, status

from api.api_v1.short_urls_api.crud import storage
from api.api_v1.short_urls_api.dependencies import prefetch_short_url
from schemas.short_url import ShortUrl

router = APIRouter(
    prefix="/{slug}",
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


@router.get("/", response_model=ShortUrl)
def get_short_url_by_slug(
    url: Annotated[
        ShortUrl,
        Depends(prefetch_short_url),
    ],
) -> ShortUrl:
    return url


@router.delete(
    "/",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_short_url(
    url: Annotated[
        ShortUrl,
        Depends(prefetch_short_url),
    ],
) -> None:
    """При удалении данных апи возвращает 204 статус код!!!"""
    storage.delete(url)
