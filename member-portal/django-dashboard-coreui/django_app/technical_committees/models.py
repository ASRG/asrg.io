from django.db import models

VIEW_STATUS_CHOICES = (
    ('Public', 'Public'),
    ('Private', 'Private'),
)

TC_STATUS_CHOICES = (
    ('Active', 'Active'),
    ('Inactive', 'Inactive'),
)

class Technical_committee(models.Model):
    name = models.CharField(max_length=150, blank=False)
    description = models.TextField(blank=False)
    short_name = models.CharField(max_length=6, blank=False)
    view_status = models.CharField(max_length= 20, choices=VIEW_STATUS_CHOICES)
    tc_status = models.CharField(max_length=15, blank=False)
    picture = models.ImageField(upload_to='technical-committee', blank=True)
