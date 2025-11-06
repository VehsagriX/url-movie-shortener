from typing import Annotated

from fastapi import Depends, APIRouter

from api.api_v1.short_urls_api.dependencies import (
    prefetch_short_url,
)
from api.api_v1.short_urls_api.crud import SHORT_URLS
from schemas.short_url import ShortUrl

router = APIRouter(
    prefix="/short-urs",
    tags=["Short URLs"],
)


@router.get(
    "/",
    response_model=list[ShortUrl],
)
def read_short_urls_list():
    return SHORT_URLS


@router.get("/{slug}/", response_model=ShortUrl)
def get_short_url_by_slug(
    url: Annotated[
        ShortUrl,
        Depends(prefetch_short_url),
    ],
) -> ShortUrl:
    return url
