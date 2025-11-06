from fastapi import APIRouter
from .short_urls_api import router as short_urls_router
from .movies_api import router as movies_router

router = APIRouter(
    prefix="/v1",
)

router.include_router(short_urls_router)
router.include_router(movies_router)
