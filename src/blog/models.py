from typing import Any

from django.contrib.auth.models import User
from django.db.models import (
    PROTECT,
    BooleanField,
    CharField,
    DateTimeField,
    ForeignKey,
    ImageField,
)
from django.utils import timezone

from tinymce.models import HTMLField

from core.models import UUIDModelMixin


class BlogPost(UUIDModelMixin):
    class Fields:
        TITLE = "title"
        AUTHOR = "author"
        IMAGE = "image"
        CONTENT = "content"
        IS_PUBLISHED = "is_published"
        CREATED_AT = "created_at"
        UPDATED_AT = "updated_at"
        PUBLISHED_AT = "published_at"

    title = CharField(max_length=30)
    author = ForeignKey(User, on_delete=PROTECT)
    image = ImageField()
    content = HTMLField(blank=True)
    is_published = BooleanField(default=False)
    created_at = DateTimeField(auto_now_add=True, editable=False)
    updated_at = DateTimeField(auto_now=True, editable=False)
    published_at = DateTimeField(default=None, null=True, blank=True)

    def save(self, *args: Any, **kwargs: Any) -> None:
        if self.is_published and not self.published_at:
            self.published_at = timezone.now()
        super(BlogPost, self).save(*args, **kwargs)
