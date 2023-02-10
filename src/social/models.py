from django.core.validators import URLValidator
from django.db.models import CharField

from core.models import UUIDModelMixin


class Social(UUIDModelMixin):
    class Fields:
        NAME = "name"
        FA_ICON = "fa_icon"
        COLOR = "color"
        LINK = "link"

    name = CharField(max_length=60)
    icon = CharField(max_length=60)
    color = CharField(max_length=60)
    link = CharField(max_length=255, validators=[URLValidator])
