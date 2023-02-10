from django.contrib import admin

from group.models import Group, GroupTag, RaidDay


class RaidDayInline(admin.TabularInline):
    model = RaidDay
    extra = 1


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    inlines = [RaidDayInline]

    list_display = (
        Group.Fields.NAME,
        Group.Fields.LEADER,
    )


@admin.register(GroupTag)
class GroupTagAdmin(admin.ModelAdmin):
    pass
