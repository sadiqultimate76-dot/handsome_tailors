from django.contrib import admin
from .models import SiteSetting


@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = (
        "site_name",
        "proprietor_name",
        "phone_primary",
        "established_year",
    )
