from django.urls import path

from recruitment.views import questionnaire_view, success_view, type_view


urlpatterns = [
    path("", type_view),
    path("zapisz/", success_view),
    path("<str:recruitment_type>/", questionnaire_view),
]
