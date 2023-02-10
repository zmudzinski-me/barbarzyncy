from django.contrib.sites.models import Site
from django.http import HttpRequest, HttpResponse
from django.template import loader

from banner.repositories import BannerRepository
from blog.repositories import BlogPostRepository
from contact.repositories import ContactRepository
from discord.client import DiscordClient
from group.repositories import GroupRepository
from raider_io.client import RaiderIOClient
from social.repositories import SocialRepository


def index(request: HttpRequest) -> HttpResponse:
    template = loader.get_template(template_name="core/home.html")

    context = {
        "site_url": Site.objects.get_current().domain,
        "social": SocialRepository.get_social(),
        "blog": BlogPostRepository.get_posts(limit=3),
        "progress": RaiderIOClient.get_progress(),
        "groups": GroupRepository.get_groups(),
        "contact": ContactRepository.get_contacts(),
        "discord_auth_link": DiscordClient.get_auth_link(),
        "banner": BannerRepository.get_banner(),
    }
    return HttpResponse(template.render(context=context))
