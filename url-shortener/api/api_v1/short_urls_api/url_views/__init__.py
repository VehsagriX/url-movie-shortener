__all__ = ("router",)


from api.api_v1.short_urls_api.url_views.list_views import router
from api.api_v1.short_urls_api.url_views.details_views import (
    router as details_short_url_router,
)

router.include_router(details_short_url_router)
