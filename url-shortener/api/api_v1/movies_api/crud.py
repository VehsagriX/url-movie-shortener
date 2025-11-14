from pydantic import BaseModel

from schemas.movie import Movie, MovieCreate

MOVIES = [
    Movie(
        slug="one",
        title="Movie 1",
        year=1999,
        description="Movie blablabla",
    ),
    Movie(
        slug="two",
        title="Movie 2",
        year=2000,
        description="Movie abcsdsa",
    ),
    Movie(
        slug="three",
        title="Movie 3",
        year=2010,
        description="Movie asdla;sdkxadasx asdkasld;as",
    ),
]


class Storage(BaseModel):
    storage_movie: dict[str, Movie] = {}

    def get(self):
        return self.storage_movie.values()

    def get_movie_by_slug(self, slug):
        return self.storage_movie[slug]

    def create_movie(self, movie_create: MovieCreate):
        movie = Movie(**movie_create.model_dump())
        self.storage_movie[movie.slug] = movie
        return movie


movie_storage = Storage()
movie_storage.create_movie(
    MovieCreate(
        slug="one",
        title="Movie 1",
        year=1999,
        description="Movie blablabla",
    ),
)

movie_storage.create_movie(
    MovieCreate(
        slug="two",
        title="Movie 2",
        year=2000,
        description="Movie abcsdsa",
    ),
)

movie_storage.create_movie(
    MovieCreate(
        slug="three",
        title="Movie 3",
        year=2010,
        description="Movie asdla;sdkxadasx asdkasld;as",
    ),
)
