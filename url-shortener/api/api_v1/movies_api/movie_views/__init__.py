from api.api_v1.movies_api.movie_views.views import router
from api.api_v1.movies_api.movie_views.details_view import router as details_router


router.include_router(details_router)
