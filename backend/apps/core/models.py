from django.db import models


class SiteSetting(models.Model):
    site_name = models.CharField(max_length=100)
    tagline = models.CharField(max_length=200)

    proprietor_name = models.CharField(max_length=100)

    phone_primary = models.CharField(max_length=20)
    phone_secondary = models.CharField(max_length=20, blank=True)

    address = models.TextField()

    established_year = models.PositiveIntegerField(default=1995)

    def __str__(self):
        return self.site_name
