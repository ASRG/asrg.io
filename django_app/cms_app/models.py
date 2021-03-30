from cms.models.pluginmodel import CMSPlugin
from django.db import models

from sponsors.models import STATUS_CHOICES


class SponsorConfig(CMSPlugin):
    name = models.CharField(max_length=50, default="Guest")
