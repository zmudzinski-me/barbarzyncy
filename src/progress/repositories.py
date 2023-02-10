from django.db.models import QuerySet

from progress.models import Progress


class ProgressRepository:
    @staticmethod
    def get_progress() -> QuerySet:
        return Progress.objects.all()
