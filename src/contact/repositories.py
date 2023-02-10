from django.db.models import Case, QuerySet, Value, When

from contact.models import Contact


class ContactRepository:
    @staticmethod
    def get_contacts() -> QuerySet:
        return Contact.objects.filter(
            rank__in=(Contact.RankChoices.GUILD_MASTER, Contact.RankChoices.OFFICER)
        ).order_by(
            Case(
                When(rank=Contact.RankChoices.GUILD_MASTER, then=Value(0)),
                When(rank=Contact.RankChoices.OFFICER, then=Value(1)),
                default=2,
            ),
            Contact.Fields.NAME,
        )
