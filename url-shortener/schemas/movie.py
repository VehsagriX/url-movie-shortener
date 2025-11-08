from typing import Annotated

from annotated_types import Len
from pydantic import BaseModel


class MovieBase(BaseModel):
    slug: str
    title: str
    description: str
    year: int


class MovieCreate(MovieBase):
    slug: Annotated[str, Len(3 - 10)]
    title: Annotated[str, Len(5, 30)]
    year: int
    description: str | None


class Movie(MovieBase):
    pass
