from typing import Annotated

from annotated_types import Len
from pydantic import BaseModel

TitleAnnotated = Annotated[str, Len(5, 30)]


class MovieBase(BaseModel):

    title: str
    description: str
    year: int


class MovieCreate(MovieBase):
    """
    Модель создания Фильма
    """

    slug: Annotated[str, Len(3 - 10)]
    title: TitleAnnotated
    year: int
    description: str | None


class MovieUpdate(MovieBase):
    """
    Модель обновления Фильма
    """

    title: TitleAnnotated


class MovieUpdatePartial(MovieBase):
    """
    Модель частичного обновления фильма
    """

    title: TitleAnnotated | None = None
    description: str | None = None
    year: int | None = None


class Movie(MovieBase):
    """
    Модель представления Фильма
    """

    slug: str
