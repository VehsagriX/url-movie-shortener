from typing import Annotated

from fastapi import APIRouter, Depends, status, BackgroundTasks


from api.api_v1.short_urls_api.crud import storage
from api.api_v1.short_urls_api.dependencies import prefetch_short_url
from schemas.short_url import (
    ShortUrl,
    ShortUrlUpdate,
    ShortUrlUpdatePartial,
    ShortUrlRead,
)

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

ShortUrlBySlug = Annotated[ShortUrl, Depends(prefetch_short_url)]


@router.get("/", response_model=ShortUrlRead)
def get_short_url_by_slug(url: ShortUrlBySlug) -> ShortUrl:
    return url


@router.delete(
    "/",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_short_url(url: ShortUrlBySlug, background_tasks: BackgroundTasks) -> None:
    """При удалении данных апи возвращает 204 статус код!!!"""

    background_tasks.add_task(storage.save_state)
    storage.delete(url)


@router.put("/", response_model=ShortUrlRead)
def update_short_url_details(
    url: ShortUrlBySlug,
    short_url_in: ShortUrlUpdate,
    background_tasks: BackgroundTasks,
):
    background_tasks.add_task(storage.save_state)
    return storage.update(short_url=url, short_url_in=short_url_in)


@router.patch("/", response_model=ShortUrlRead)
def update_short_url_details_partial(
    url: ShortUrlBySlug,
    short_url_in: ShortUrlUpdatePartial,
    background_tasks: BackgroundTasks,
):
    background_tasks.add_task(storage.save_state)
    return storage.update_partial(short_url=url, short_url_in=short_url_in)
