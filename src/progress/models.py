from django.db.models import CharField, ImageField

from core.models import UUIDModelMixin


class Progress(UUIDModelMixin):
    class Fields:
        RAID_NAME = "raid_name"
        RAID_KEY = "raid_key"
        IMAGE = "image"

    raid_name = CharField(max_length=255)
    raid_key = CharField(max_length=255)
    image = ImageField()
