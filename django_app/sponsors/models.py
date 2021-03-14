from imagekit.models import ImageSpecField, ProcessedImageField
from django.db import models


STATUS_CHOICES = (
    ("active", "Active"),
    ("not-active", "Not active"),
)


class Sponsor(models.Model):
    name = models.CharField(max_length=160, blank=False, primary_key=True)
    website = models.URLField(blank=True, verbose_name="Sponsor website")
    address = models.TextField(blank=True)
    description = models.TextField(blank=False)
    email = models.EmailField(verbose_name="General email address", blank=True)
    start_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default=STATUS_CHOICES[1][0]
    )
    logo = ProcessedImageField(
        upload_to="sponsors/logos", blank=True, verbose_name="Company Logo"
    )

    def __str__(self):
        return self.name
