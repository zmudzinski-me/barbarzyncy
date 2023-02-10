from django.urls import path

from blog.views import BlogListView, BlogView


urlpatterns = [
    path("", BlogListView.as_view()),
    path("<uuid:id>/", BlogView.as_view()),
]
