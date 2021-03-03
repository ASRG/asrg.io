from imagekit.models import ImageSpecField, ProcessedImageField
from django.db import models


class Sponsor(models.Model):
    logo = ProcessedImageField(
        upload_to="sponsors/logos", blank=True, verbose_name="Company Logo"
    )
    name = models.CharField(max_length=160, blank=False)
    description = models.TextField(blank=False, verbose_name="Bio")

    def __str__(self):
        return self.name
