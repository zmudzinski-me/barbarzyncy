from typing import Optional

from django.db.models import QuerySet

from social.models import Social


class SocialRepository:
    @staticmethod
    def get_social() -> QuerySet:
        return Social.objects.all()

    @staticmethod
    def get_social_link(name: str) -> Optional[str]:
        try:
            return Social.objects.get(name=name).link
        except Social.DoesNotExist:
            return None
