from django.db.models import CharField, DateTimeField, TextChoices, TextField

from core.models import UUIDModelMixin


class Question(UUIDModelMixin):
    class Fields:
        RECRUITMENT_TYPE = "recruitment_type"
        CONTENT = "content"
        INPUT_TYPE = "input_type"

    class RecruitmentType(TextChoices):
        PVE = "pve"
        CASUAL = "casual"

    class InputType(TextChoices):
        TEXT = "text"
        MULTILINE = "multiline"
        RADIO = "radio"

    recruitment_type = CharField(
        max_length=10, choices=RecruitmentType.choices, default=RecruitmentType.CASUAL
    )
    input_type = CharField(
        max_length=10, choices=InputType.choices, default=InputType.TEXT
    )
    content = TextField()


class Questionnaire(UUIDModelMixin):
    class Fields:
        DISCORD = "discord"
        CREATED_AT = "created_at"

    discord = CharField(max_length=255)
    created_at = DateTimeField(auto_now_add=True)
