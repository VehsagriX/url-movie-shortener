import logging

from pydantic import BaseModel, ValidationError

from core.config import SHORT_URL_STORAGE_FILEPATH
from schemas.short_url import (
    ShortUrl,
    ShortUrlCreate,
    ShortUrlUpdate,
    ShortUrlUpdatePartial,
)


log = logging.getLogger(__name__)


class ShortUrlsStorage(BaseModel):
    slug_to_short_url: dict[str, ShortUrl] = {}

    def save_state(self):
        SHORT_URL_STORAGE_FILEPATH.write_text(self.model_dump_json(indent=2))
        log.info("Saved shorturl to storage file.")

    @classmethod
    def from_state(cls) -> "ShortUrlsStorage":
        if not SHORT_URL_STORAGE_FILEPATH.exists():
            log.info("No shorturl storage file.")
            return ShortUrlsStorage()
        return cls.model_validate_json(SHORT_URL_STORAGE_FILEPATH.read_text())

    def init_url_storage_from_state(self) -> None:
        try:
            data = ShortUrlsStorage().from_state()
            log.info("ShortUrlsStorage loaded from state.")
        except ValidationError:
            self.save_state()
            log.warning("Rewriting shorturl storage file. Validation error.")
            return

        self.slug_to_short_url.update(
            data.slug_to_short_url,
        )

    def get(self) -> list[ShortUrl]:
        return list(self.slug_to_short_url.values())

    def get_by_slug(self, slug: str) -> ShortUrl | None:
        return self.slug_to_short_url.get(slug)

    def create(self, short_url_create: ShortUrlCreate) -> ShortUrl:
        short_url = ShortUrl(
            **short_url_create.model_dump(),
        )
        self.slug_to_short_url[short_url.slug] = short_url
        log.info("Created shorturl")
        return short_url

    def delete_by_slug(self, slug) -> None:
        self.slug_to_short_url.pop(slug, None)

    def delete(self, short_url: ShortUrl) -> None:
        self.delete_by_slug(short_url.slug)

    def update(self, short_url: ShortUrl, short_url_in: ShortUrlUpdate) -> ShortUrl:
        for field_name, value in short_url_in:
            setattr(short_url, field_name, value)
        return short_url

    def update_partial(
        self, short_url: ShortUrl, short_url_in: ShortUrlUpdatePartial
    ) -> ShortUrl:
        for field_name, value in short_url_in.model_dump(exclude_unset=True).items():
            setattr(short_url, field_name, value)
        return short_url


storage = ShortUrlsStorage()


# storage.create(
#     ShortUrlCreate(
#         target_url=AnyHttpUrl("https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
#         slug="Youtube",
#     ),
# )
# storage.create(
#     ShortUrlCreate(
#         target_url=AnyHttpUrl("https://google.com"),
#         slug="Google",
#     ),
# )
