import logging
from pathlib import Path


BASE_DIR = (
    Path(__file__).resolve().parent.parent
)  ## Выходим к url-shortener основная папка проекта src

SHORT_URL_STORAGE_FILEPATH = BASE_DIR / "short-url.json"

MOVIE_STORAGE_FILEPATH = BASE_DIR / "movie.json"

LOG_LVL = logging.INFO

LOG_FORMAT: str = (
    "[%(asctime)s.%(msecs)03d]  %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s"
)
