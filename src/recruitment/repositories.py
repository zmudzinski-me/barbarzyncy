from django.db.models import QuerySet

from recruitment.models import Question, Questionnaire


class RecruitmentRepository:
    @staticmethod
    def get_questions(recruitment_type: str) -> QuerySet:
        try:
            type_enum = Question.RecruitmentType(recruitment_type)
            return Question.objects.filter(recruitment_type=type_enum)
        except ValueError:
            return Question.objects.none()

    @staticmethod
    def check_questionnaire_exists(discord: str) -> None:
        if Questionnaire.objects.filter(discord=discord).exists():
            raise ValueError("Już składałeś podanie. Poczekaj na kontakt od Szamana.")

    @staticmethod
    def save(discord: str) -> None:
        Questionnaire.objects.create(discord=discord)
