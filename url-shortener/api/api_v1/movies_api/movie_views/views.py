import logging

from fastapi import status, APIRouter
from starlette.background import BackgroundTasks

from api.api_v1.movies_api.crud import movie_storage
from schemas.movie import MovieCreate, MovieRead, Movie


log = logging.getLogger(__name__)

router = APIRouter(
    prefix="/movies",
    tags=["Movies"],
)


@router.get(
    "/",
    response_model=list[MovieRead],
)
def read_movies() -> list[Movie]:
    return movie_storage.get()


@router.post(
    "/",
    response_model=MovieRead,
    status_code=status.HTTP_201_CREATED,
)
def create_movie(movie_create: MovieCreate, background_tasks: BackgroundTasks) -> Movie:
    background_tasks.add_task(movie_storage.save_state)
    log.info("Return created movie and save state")
    return movie_storage.create_movie(movie_create)
