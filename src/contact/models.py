from django.db.models import CharField, TextChoices

from battle_net.client import BattleNetClient
from core.models import UUIDModelMixin


class Contact(UUIDModelMixin):
    class Fields:
        NAME = "name"
        RANK = "rank"
        DISCORD = "discord"
        SERVER = "server"
        CHARACTER_NAME = "character_name"
        WOW_IMAGE = "wow_image"

    class RankChoices(TextChoices):
        GUILD_MASTER = "Ojciec Barbarzyńca"
        OFFICER = "Szaman"
        RAID_LEADER = "Raid Leader"

    name = CharField(max_length=30)
    rank = CharField(choices=RankChoices.choices, max_length=18)
    discord = CharField(max_length=37)
    server = CharField(max_length=30, null=True, blank=True)
    character_name = CharField(max_length=12, null=True, blank=True)
    wow_image = CharField(max_length=255, null=True, blank=True, editable=False)

    def save(self, *args, **kwargs):
        if self.server and self.character_name:
            self.server = self.server.lower().replace(" ", "-")
            self.character_name = self.character_name.lower()
            self.wow_image = BattleNetClient.get_character_avatar(
                name=self.character_name,
                server=self.server,
            )
        super(Contact, self).save(*args, **kwargs)
