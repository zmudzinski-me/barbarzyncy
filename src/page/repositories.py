from typing import Optional

from page.models import Page


class PageRepository:
    _ERROR_PAGE_SLUG = "404"

    @staticmethod
    def get_by_slug(slug: str) -> Optional[Page]:
        try:
            return Page.objects.get(slug=slug)
        except Page.DoesNotExist:
            return None

    @classmethod
    def get_error_page(cls) -> Optional[Page]:
        return cls.get_by_slug(slug=cls._ERROR_PAGE_SLUG)
