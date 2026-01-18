from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from apps.pages.views import (
    home_view,
    about_view,
    gallery_view,
    contact_view,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_view, name="home"),
    path("about/", about_view, name="about"),
    path("gallery/", gallery_view, name="gallery"),
    path("contact/", contact_view, name="contact"),
]

# MEDIA files (ONLY for development)
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
