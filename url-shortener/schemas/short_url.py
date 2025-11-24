from typing import Annotated
from annotated_types import Len, MaxLen
from pydantic import BaseModel, AnyHttpUrl


DescriptionAnnotated = Annotated[str, MaxLen(100)]


class ShortUrlBase(BaseModel):
    target_url: AnyHttpUrl
    description: DescriptionAnnotated = ""


class ShortUrlCreate(ShortUrlBase):
    """
    Модель для создания сокращенной ссылки
    """

    slug: Annotated[str, Len(3, 10)]


class ShortUrlUpdatePartial(ShortUrlBase):
    """
    Модель частичного обновления ссылки
    """

    target_url: AnyHttpUrl | None = None
    description: DescriptionAnnotated | None = None


class ShortUrlUpdate(ShortUrlBase):
    """
    Модель обновления ссылки
    """

    description: DescriptionAnnotated


class ShortUrl(ShortUrlBase):
    """
    Модель сокращенной ссылки
    """

    slug: str
