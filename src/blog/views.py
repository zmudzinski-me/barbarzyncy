from typing import Any, Dict
from uuid import UUID

from django.contrib.sites.models import Site
from django.db.models import QuerySet
from django.http import Http404
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from blog.models import BlogPost
from blog.repositories import BlogPostRepository


class BlogView(TemplateView):
    template_name = "blog/blog.html"

    def get_context_data(self, id: UUID, **kwargs: Any) -> Dict[str, Any]:
        try:
            blog_post = BlogPostRepository.get_by_id(id=id)
        except BlogPost.DoesNotExist:
            raise Http404("Blog page does not exist")

        context = super().get_context_data(**kwargs)
        context["blog_post"] = blog_post
        context["site_url"] = Site.objects.get_current().domain
        return context


class BlogListView(ListView):
    template_name = "blog/blog_list.html"
    model = BlogPost
    paginate_by = 12

    def get_queryset(self) -> QuerySet:
        return BlogPostRepository.get_posts()

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["site_url"] = Site.objects.get_current().domain
        return context
