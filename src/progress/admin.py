from django.contrib import admin

from progress.models import Progress


@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = (
        Progress.Fields.RAID_NAME,
        Progress.Fields.RAID_KEY,
    )
