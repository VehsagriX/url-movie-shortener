from schemas.short_url import ShortUrl, ShortUrlCreate
from pydantic import AnyHttpUrl, BaseModel


class ShortUrlsStorage(BaseModel):
    slug_to_short_url: dict[str, ShortUrl] = {}

    def get(self) -> list[ShortUrl]:
        return list(self.slug_to_short_url.values())

    def get_by_slug(self, slug: str) -> ShortUrl | None:
        return self.slug_to_short_url.get(slug)

    def create(self, short_url_create: ShortUrlCreate) -> ShortUrl:
        short_url = ShortUrl(
            **short_url_create.model_dump(),
        )
        self.slug_to_short_url[short_url.slug] = short_url
        return short_url

    def delete_by_slug(self, slug) -> None:
        self.slug_to_short_url.pop(slug, None)

    def delete(self, short_url: ShortUrl) -> None:
        self.delete_by_slug(short_url.slug)


storage = ShortUrlsStorage()

storage.create(
    ShortUrlCreate(
        target_url=AnyHttpUrl("https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
        slug="Youtube",
    ),
)
storage.create(
    ShortUrlCreate(
        target_url=AnyHttpUrl("https://google.com"),
        slug="Google",
    ),
)
