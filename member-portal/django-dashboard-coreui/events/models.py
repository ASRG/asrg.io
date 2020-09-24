from django.db import models

from core.settings import CHAPTERS
from authentication.models import Chapter, User
from .timezones import TIMEZONES as TIMEZONE_CHOICES

EVENT_TYPE_CHOICES = (
    ('Webinar', 'Webinar'),
    ('Meeting', 'Meeting'),
    ('CTF', 'CTF'),
    ('Workshop', 'Workshop'),
    ('Conference', 'Conference'),
    ('Tournament', 'Tournament'),
)

MODE_CHOICES = (
    ('Internal', 'Internal'),
    ('External', 'External'),
)

STATUS_CHOICES = (
    ("1", "In Plan"),
    ("2", "Confirmed"),
    ("3", "Invited"),
    ("4", "Completed"),
    ("5", "Cancelled"),
)

class Event(models.Model):
    title = models.CharField(max_length=80, blank=False)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)
    event_type = models.CharField(max_length=11, choices=EVENT_TYPE_CHOICES)
    mode = models.CharField(max_length=9, choices=MODE_CHOICES)
    location = models.ForeignKey('authentication.Chapter', related_name='event', on_delete=models.CASCADE)
    host = models.CharField(max_length=50, blank=True)
    presenter_first_name = models.CharField(max_length=50, blank=False, verbose_name='First Name')
    presenter_last_name = models.CharField(max_length=50, blank=False, verbose_name='Last Name')
    presenter_designation = models.CharField(max_length=80, blank=False, verbose_name='Designation')
    presenter_picture = models.ImageField(upload_to='events/presenters', blank=False)
    presenter_profile_url = models.URLField(blank=False, verbose_name='Public Profile URL')
    presenter_company_name = models.CharField(max_length=100, blank=False, verbose_name='Company Name')
    presenter_company_logo = models.ImageField(upload_to='events/company logos', blank=False, verbose_name='Company Logo')
    presenter_company_website = models.URLField(blank=True, verbose_name='Company Website')
    presenter_bio = models.TextField(blank=False, verbose_name='Bio')
    event_description = models.TextField(blank=False)
    event_address = models.TextField(blank=True)
    link = models.URLField(blank=True)
    timezone = models.CharField(max_length=30, blank=False, choices=TIMEZONE_CHOICES)
    start_date = models.DateField(blank=False)
    start_time = models.TimeField(blank=False)
    end_date = models.DateField(blank=False)
    end_time = models.TimeField(blank=False)

    added_by = models.ForeignKey("authentication.User", related_name='event', on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

