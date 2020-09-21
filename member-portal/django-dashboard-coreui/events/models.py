from django.db import models

from core.settings import CHAPTERS
from authentication.models import Chapter, User

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
    presenter_picture = models.ImageField(upload_to='events/presenters', blank=False)
    presenter_company_name = models.CharField(max_length=100, blank=False, verbose_name='Company Name')
    presenter_company_logo = models.ImageField(upload_to='events/company logos', blank=False, verbose_name='Company Logo')
    presenter_bio = models.TextField(blank=False, verbose_name='Bio')
    event_address = models.TextField(blank=False)
    link = models.URLField(blank=True)
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()

    added_by = models.ForeignKey("authentication.User", related_name='event', on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

