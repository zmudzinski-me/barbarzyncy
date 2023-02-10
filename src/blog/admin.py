from django.contrib import admin

from blog.models import BlogPost
from core.models import UUIDModelMixin


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        UUIDModelMixin.Fields.ID,
        BlogPost.Fields.TITLE,
        BlogPost.Fields.AUTHOR,
        BlogPost.Fields.CREATED_AT,
        BlogPost.Fields.IS_PUBLISHED,
    )
