from django.contrib.sites.models import Site
from django.http import Http404, HttpRequest, HttpResponse
from django.template import loader

from page.repositories import PageRepository


def page_view(request: HttpRequest, slug: str) -> HttpResponse:
    page = PageRepository.get_by_slug(slug=slug)
    if not page:
        raise Http404("Page does not exist")

    template = loader.get_template(template_name="page/page.html")

    context = {"page": page, "site_url": Site.objects.get_current().domain}
    return HttpResponse(template.render(context=context))


def error_view(request: HttpRequest, exception: ValueError) -> HttpResponse:
    page = PageRepository.get_error_page()
    template = loader.get_template(template_name="page/page.html")
    context = {"page": page, "site_url": Site.objects.get_current().domain}
    return HttpResponse(template.render(context=context))


def crash_view(request: HttpRequest) -> HttpResponse:
    page = PageRepository.get_error_page()
    template = loader.get_template(template_name="page/page.html")
    context = {"page": page, "site_url": Site.objects.get_current().domain}
    return HttpResponse(template.render(context=context))
