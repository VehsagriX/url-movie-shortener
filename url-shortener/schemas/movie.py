from typing import Annotated

from annotated_types import Len
from pydantic import BaseModel

TitleAnnotated = Annotated[str, Len(5, 30)]


class MovieBase(BaseModel):

    title: str
    description: str
    year: int


class MovieCreate(MovieBase):
    slug: Annotated[str, Len(3 - 10)]
    title: TitleAnnotated
    year: int
    description: str | None


class MovieUpdate(MovieBase):
    title: TitleAnnotated


class MovieUpdatePartial(MovieBase):
    title: TitleAnnotated | None = None
    description: str | None = None
    year: int | None = None


class Movie(MovieBase):
    slug: str
