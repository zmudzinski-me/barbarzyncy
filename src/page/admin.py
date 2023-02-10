from django.contrib import admin

from page.models import Page


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = (
        Page.Fields.TITLE,
        Page.Fields.SLUG,
        Page.Fields.CREATED_AT,
        Page.Fields.UPDATED_AT,
    )
