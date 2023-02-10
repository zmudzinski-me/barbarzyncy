from django.contrib import admin

from recruitment.models import Question, Questionnaire


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        Question.Fields.CONTENT,
        Question.Fields.RECRUITMENT_TYPE,
        Question.Fields.INPUT_TYPE,
    )
    list_filter = (Question.Fields.RECRUITMENT_TYPE,)


@admin.register(Questionnaire)
class QuestionnaireAdmin(admin.ModelAdmin):
    list_display = (
        Questionnaire.Fields.DISCORD,
        Questionnaire.Fields.CREATED_AT,
    )
    readonly_fields = (
        Questionnaire.Fields.DISCORD,
        Questionnaire.Fields.CREATED_AT,
    )
    search_fields = (Questionnaire.Fields.DISCORD,)

    def has_add_permission(self, request):
        return False
