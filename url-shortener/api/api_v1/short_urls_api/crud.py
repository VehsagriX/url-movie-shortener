from schemas.short_url import ShortUrl
from pydantic import AnyHttpUrl

SHORT_URLS = [
    ShortUrl(
        target_url=AnyHttpUrl("https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
        slug="Youtube",
    ),
    ShortUrl(
        target_url=AnyHttpUrl("https://google.com"),
        slug="Google",
    ),
]
