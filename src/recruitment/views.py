from typing import Optional

from django.contrib.sites.models import Site
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.template import loader

from discord.client import DiscordClient
from recruitment.repositories import RecruitmentRepository
from social.repositories import SocialRepository


def type_view(request: HttpRequest) -> HttpResponse:
    code = request.GET.get("code")
    if not code:
        raise Http404("Code missing")
    template = loader.get_template(template_name="recruitment/type.html")
    context = {
        "code": code,
        "site_url": Site.objects.get_current().domain,
    }
    return HttpResponse(template.render(context=context, request=request))


def questionnaire_view(request: HttpRequest, recruitment_type: str) -> HttpResponse:
    token_type = request.session.get("token_type")
    access_token = request.session.get("access_token")

    if not (token_type and access_token):
        code = request.GET.get("code")
        if not code:
            raise Http404("Code missing")
        token_type, access_token = DiscordClient.exchange_token(code=code)
        request.session["token_type"] = token_type
        request.session["access_token"] = access_token

    error: Optional[str] = None
    answers = {}
    questions = RecruitmentRepository.get_questions(recruitment_type=recruitment_type)
    if not questions:
        raise Http404("Questions do not exist")

    if request.method == "POST":
        try:
            for question in questions:
                answers[question.id] = request.POST[str(question.id)]

            DiscordClient.send_quesionnaire(
                questions=questions,
                answers=answers,
                recruitment_type=recruitment_type,
                token_type=token_type,
                access_token=access_token,
            )
            return redirect(success_view)

        except ValueError as cause:
            error = str(cause)

    template = loader.get_template(template_name="recruitment/questionnaire.html")
    context = {
        "recruitment_type": recruitment_type,
        "error": error,
        "questions": questions,
        "answers": answers,
        "site_url": Site.objects.get_current().domain,
    }
    return HttpResponse(template.render(context=context, request=request))


def success_view(request: HttpRequest) -> HttpResponse:
    template = loader.get_template(template_name="recruitment/done.html")
    context = {
        "site_url": Site.objects.get_current().domain,
        "discord_url": SocialRepository.get_social_link(name="Discord"),
    }
    return HttpResponse(template.render(context=context, request=request))
