from django.db import models


class Events(models.Model):
    title = models.CharField(max_length=80)
    presenter = models.CharField(max_length=120)
    presenter_company = models.CharField(max_length=120)
    presenter_info = models.TextField(blank=True)
    present_date = models.DateTimeField()
    description = models.TextField(blank=True)
