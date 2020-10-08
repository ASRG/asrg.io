from django.db import models
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill


class JobPosting(models.Model):
    title = models.CharField(max_length=80)
    job_category = models.CharField(max_length=120)
    location = models.CharField(max_length=56, null=False, blank=False)
    date_posted = models.DateTimeField(blank=True, auto_now_add=True)
    job_description = models.TextField(blank=True)
    job_link = models.URLField(blank=True, verbose_name="Job Posting Link")
    company_name = models.CharField(max_length=80)

class Contributor(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    linkedin = models.URLField(max_length=200)
    github = models.URLField(max_length=200)
    img = ProcessedImageField(upload_to="contributors",verbose_name='Image',blank=False)
    image_thumbnail = ImageSpecField(source='img', processors=[ResizeToFill(120, 120)], format='JPEG')
    def __str__(self):
        return self.name


class Announcement(models.Model):
    title = models.CharField(max_length=100)
    announcement = models.TextField(max_length=300)
    date_posted = models.DateTimeField(blank=True, auto_now_add=True)
    def __str__(self):
        return self.title
