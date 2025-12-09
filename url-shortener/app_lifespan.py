from contextlib import asynccontextmanager

from fastapi import FastAPI

from api.api_v1.movies_api.crud import movie_storage
from api.api_v1.short_urls_api.crud import storage


@asynccontextmanager
async def lifespan(app: FastAPI):
    # действие до запуска приложения
    storage.init_url_storage_from_state()
    movie_storage.init_movie_state()
    # ставим приложение на паузу
    yield
    # выполняем завершение работы
    # сохраняем изменение в файл и закрываем соединение
