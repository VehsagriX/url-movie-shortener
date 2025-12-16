import logging

from pydantic import BaseModel, ValidationError
from core.config import MOVIE_STORAGE_FILEPATH
from schemas.movie import Movie, MovieCreate, MovieUpdate, MovieUpdatePartial


log = logging.getLogger(__name__)


class MovieStorage(BaseModel):
    storage_movie: dict[str, Movie] = {}

    def save_state(self):
        MOVIE_STORAGE_FILEPATH.write_text(self.model_dump_json(indent=2))
        log.info("Saved state to movie storage")

    @classmethod
    def from_state(cls) -> "MovieStorage":
        if not MOVIE_STORAGE_FILEPATH.exists():
            log.info("No movie storage file.")
            return MovieStorage()
        return cls.model_validate_json(MOVIE_STORAGE_FILEPATH.read_text())

    def init_movie_from_state(self) -> None:
        try:
            movie_data = MovieStorage().from_state()
            log.warning("Movie storage loaded successfully")
        except ValidationError:
            self.save_state()
            log.warning("Movie storage could not be loaded, but we rewriting it")
            return

        self.storage_movie.update(
            movie_data.storage_movie,
        )

    def get(self):
        return self.storage_movie.values()

    def get_movie_by_slug(self, slug):
        return self.storage_movie.get(slug)

    def create_movie(self, movie_create: MovieCreate):
        movie = Movie(**movie_create.model_dump())
        self.storage_movie[movie.slug] = movie
        log.info("Created Movie %s", movie.title)

        return movie

    def delete_movie_by_slug(self, slug) -> None:
        self.storage_movie.pop(slug)
        self.save_state()

    def delete_movie(self, movie: Movie) -> None:
        self.delete_movie_by_slug(movie.slug)

    def update(self, movie: Movie, movie_in: MovieUpdate) -> Movie:
        for field_name, value in movie_in:
            setattr(movie, field_name, value)
        self.save_state()
        return movie

    def update_partial(self, movie: Movie, movie_in: MovieUpdatePartial) -> Movie:
        for field_name, value in movie_in.model_dump(exclude_unset=True).items():
            setattr(movie, field_name, value)
        self.save_state()
        return movie


movie_storage = MovieStorage()


# movie_storage = Storage()
# movie_storage.create_movie(
#     MovieCreate(
#         slug="one",
#         title="Movie 1",
#         year=1999,
#         description="Movie blablabla",
#     ),
# )
#
# movie_storage.create_movie(
#     MovieCreate(
#         slug="two",
#         title="Movie 2",
#         year=2000,
#         description="Movie abcsdsa",
#     ),
# )
#
# movie_storage.create_movie(
#     MovieCreate(
#         slug="three",
#         title="Movie 3",
#         year=2010,
#         description="Movie asdla;sdkxadasx asdkasld;as",
#     ),
# )
