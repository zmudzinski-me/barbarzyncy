from django.db.models import (
    PROTECT,
    BooleanField,
    CharField,
    ForeignKey,
    ManyToManyField,
    OneToOneField,
    TextChoices,
    TimeField,
)

from contact.models import Contact
from core.models import UUIDModelMixin


class GroupTag(UUIDModelMixin):
    class Fields:
        NAME = "name"

    name = CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Group(UUIDModelMixin):
    class Fields:
        NAME = "name"
        TAGS = "tags"
        RAID_DAYS = "raid_days"
        LEADER = "leader"

    name = CharField(max_length=30, unique=True)
    tags = ManyToManyField(
        GroupTag, related_name=Fields.TAGS, related_query_name=Fields.TAGS
    )
    leader = OneToOneField(
        Contact,
        unique=True,
        on_delete=PROTECT,
        related_name=Fields.LEADER,
        related_query_name=Fields.LEADER,
    )


class RaidDay(UUIDModelMixin):
    class Fields:
        DAY_OF_WEEK = "day_of_week"
        TIME_START = "time_start"
        TIME_END = "time_end"
        GROUP = "group"
        IS_REQUIRED = "is_required"

    class DayChoices(TextChoices):
        MONDAY = "monday", "Poniedziałek"
        TUESDAY = "tuesday", "Wtorek"
        WEDNESDAY = "wednesday", "Środa"
        THURSDAY = "thursday", "Czwartek"
        FRIDAY = "friday", "Piątek"
        SATURDAY = "saturday", "Sobota"
        SUNDAY = "sunday", "Niedziela"

    day_of_week = CharField(max_length=9, choices=DayChoices.choices)
    time_start = TimeField()
    time_end = TimeField()
    group = ForeignKey(
        Group,
        on_delete=PROTECT,
        related_name=Group.Fields.RAID_DAYS,
        related_query_name=Group.Fields.RAID_DAYS,
    )
    is_required = BooleanField(default=True)
