from django.db import models


class JobPosting(models.Model):
    title = models.CharField(max_length=80)
    job_category = models.CharField(max_length=120)
    location = models.CharField(max_length=56, null=False, blank=False)
    date_posted = models.DateTimeField(blank=True, auto_now_add=True)
    job_description = models.TextField(blank=True)

class Contributor(models.Model):
    name = models.CharField(max_length=200)
    linkedin = models.URLField(max_length=200)
    github = models.URLField(max_length=200)
    def __str__(self):
        return self.name