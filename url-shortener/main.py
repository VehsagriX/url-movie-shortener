import logging

from fastapi import (
    FastAPI,
    Request,
)

from api import router as api_router
from core.config import LOG_FORMAT, LOG_LVL

logging.basicConfig(
    level=LOG_LVL,
    format=LOG_FORMAT,
    filename="url-shortener.log",
    filemode="w",
    encoding="utf-8",
    datefmt="%d/%m/%Y %I:%M:%S %p",
)

app = FastAPI(
    title="URL, Movie Shortener",
)
app.include_router(api_router)


@app.get("/")
def reed_root(request: Request, name: str = "World"):
    docs_url = request.url.replace(
        path="/docs",
        query="",
    )
    return {"message": f"Hello {name}", "docs": str(docs_url)}
