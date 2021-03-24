from django.db import models

from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill


class Contributor(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    linkedin = models.URLField(max_length=200)
    github = models.URLField(max_length=200)
    img = ProcessedImageField(upload_to="contributors", verbose_name='Image', blank=False)
    image_thumbnail = ImageSpecField(source='img', processors=[ResizeToFill(120, 120)], format='JPEG')

    def __str__(self):
        return self.name
