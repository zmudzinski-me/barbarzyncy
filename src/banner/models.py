from typing import Any

from django.db.models import BooleanField, CharField, URLField

from core.models import UUIDModelMixin


class Banner(UUIDModelMixin):
    class Fields:
        TITLE = "title"
        DESCRIPTION = "description"
        LINK = "link"
        IS_ACTIVE = "is_active"

    title = CharField(max_length=60)
    description = CharField(max_length=120)
    link = URLField()
    is_active = BooleanField(default=False)

    def save(self, *args: Any, **kwargs: Any) -> None:
        if self.is_active:
            try:
                old_banner = Banner.objects.get(is_active=True)
                old_banner.is_active = False
                old_banner.save()
            except Banner.DoesNotExist:
                pass
        super(Banner, self).save(*args, **kwargs)
