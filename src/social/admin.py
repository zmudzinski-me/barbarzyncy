from django.contrib import admin

from social.models import Social


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = (
        Social.Fields.NAME,
        Social.Fields.LINK,
    )
