from django.urls import path

from page.views import page_view


urlpatterns = [
    path("<str:slug>/", page_view),
]
