from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles import views
from django.urls import include, path, re_path
from django.views.static import serve


urlpatterns = [
    path("admin/", admin.site.urls),
    path("tinymce/", include("tinymce.urls")),
    path("", include("core.urls")),
    path("rekrutacja/", include("recruitment.urls")),
    path("blog/", include("blog.urls")),
    path("", include("page.urls")),
]

handler400 = "page.views.error_view"
handler403 = "page.views.error_view"
handler404 = "page.views.error_view"
handler500 = "page.views.crash_view"


if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path(r"__debug__/", include(debug_toolbar.urls)),
        re_path(r"^static/(?P<path>.*)$", views.serve),
        re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    ]
