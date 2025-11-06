from fastapi import APIRouter


from .api_v1 import router as v1_router
from .redirect_views import router as redirect_views

router = APIRouter(prefix="/api")

router.include_router(v1_router)
router.include_router(redirect_views)
