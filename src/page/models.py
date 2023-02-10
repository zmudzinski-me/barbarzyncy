from django.db.models import CharField, DateTimeField

from tinymce.models import HTMLField

from core.models import UUIDModelMixin


class Page(UUIDModelMixin):
    class Fields:
        TITLE = "title"
        SLUG = "slug"
        CONTENT = "content"
        CREATED_AT = "created_at"
        UPDATED_AT = "updated_at"

    title = CharField(max_length=30)
    slug = CharField(max_length=30, unique=True)
    content = HTMLField(blank=True)
    created_at = DateTimeField(auto_now_add=True, editable=False)
    updated_at = DateTimeField(auto_now=True, editable=False)
