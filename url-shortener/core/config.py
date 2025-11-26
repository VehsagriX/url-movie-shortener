from pathlib import Path


BASE_DIR = (
    Path(__file__).resolve().parent.parent
)  ## Выходим к url-shortener основная папка проекта src

SHORT_URL_STORAGE_FILEPATH = BASE_DIR / "short-url.json"

MOVIE_STORAGE_FILEPATH = BASE_DIR / "movie.json"
