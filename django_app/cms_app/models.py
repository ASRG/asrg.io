from cms.models.pluginmodel import CMSPlugin
from django.db import models

from sponsors.models import STATUS_CHOICES


class SponsorConfig(CMSPlugin):
    name = models.CharField(max_length=50, default="Guest")


class CounterConfig(CMSPlugin):
    member_offset = models.IntegerField(default=5657)
    locations_offset = models.IntegerField(default=0)
    meetings_offset = models.IntegerField(default=0)
