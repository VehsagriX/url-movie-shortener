from fastapi import APIRouter, status, BackgroundTasks

from api.api_v1.short_urls_api.crud import storage
from schemas.short_url import ShortUrl, ShortUrlCreate, ShortUrlRead

router = APIRouter(
    prefix="/short-urs",
    tags=["Short URLs"],
)


@router.get(
    "/",
    response_model=list[ShortUrlRead],
)
def read_short_urls_list() -> list[ShortUrl]:
    return storage.get()


@router.post(
    "/",
    response_model=ShortUrlRead,
    status_code=status.HTTP_201_CREATED,
)
def create_short_url(
    short_url_create: ShortUrlCreate,
    background_tasks: BackgroundTasks,
) -> ShortUrl:
    """При создании данных апи возвращает 201 статус код!!!"""
    background_tasks.add_task(storage.save_state)
    return storage.create(short_url_create)
