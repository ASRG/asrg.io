from django.db import models


class Events(models.Model):
    EVENT_STATUS = [('1', 'In Plan'), ('2', 'Confirmed'),
                    ('3', 'Invited'), ('4', 'Completed'), ('5', 'Cancelled')]

    event_status = models.CharField(
        max_length=1, choices=EVENT_STATUS, blank=False)
    join_link = models.URLField(max_length=400)
    title = models.CharField(max_length=80)
    presenter = models.CharField(max_length=120)
    presenter_company = models.CharField(max_length=120)
    presenter_info = models.TextField(blank=True)
    present_date = models.DateTimeField()
    description = models.TextField(blank=True)
    location = models.CharField(max_length=10)

    def __str__(self):
        return self.title


class Projects(models.Model):
    PROJECT_STATUS = [('1', 'Searching for Team Members'), ('2', 'In Progress'),
                      ('3', 'Completed')]

    project_status = models.CharField(
        max_length=1, choices=PROJECT_STATUS, blank=False)
    join_project_link = models.URLField(max_length=400)
    project_name = models.CharField(max_length=120)
    project_short_name = models.CharField(max_length=10)
    project_lead = models.CharField(max_length=200)
    project_image = models.ImageField(
        upload_to=None, height_field=None, width_field=None, max_length=100,)
    project_description = models.TextField(blank=True)

    def __str__(self):
        return self.project_name
