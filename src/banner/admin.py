from django.contrib import admin

from banner.models import Banner
from core.models import UUIDModelMixin


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = (
        UUIDModelMixin.Fields.ID,
        Banner.Fields.TITLE,
        Banner.Fields.DESCRIPTION,
        Banner.Fields.IS_ACTIVE,
    )
    ordering = (f"-{Banner.Fields.IS_ACTIVE}",)
