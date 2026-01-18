from django.shortcuts import render
from apps.core.models import SiteSetting


def home_view(request):
    site = SiteSetting.objects.first()
    return render(request, "pages/home.html", {
        "site": site
    })


def contact_view(request):
    site = SiteSetting.objects.first()
    return render(request, "pages/contact.html", {
        "site": site
    })


def about_view(request):
    site = SiteSetting.objects.first()
    return render(request, "pages/about.html", {
        "site": site
    })


def gallery_view(request):
    site = SiteSetting.objects.first()
    return render(request, "pages/gallery.html", {
        "site": site
    })
