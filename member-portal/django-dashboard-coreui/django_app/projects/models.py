from django.db import models

# Create your models here.

VIEW_STATUS_CHOICES = (
    ('Public', 'Public'),
    ('Private', 'Private'),
)

PROJECT_STATUS_CHOICES = (
    ('Planning Phase', 'Planning Phase'),
    ('In Progress', 'In Progress'),
    ('Completed', 'Completed'),
)
class Project(models.Model):
    name = models.CharField(max_length=150, blank=False)
    description = models.TextField(blank=False)
    short_name = models.CharField(max_length=6, blank=False)
    view_status = models.CharField(max_length= 20, choices=VIEW_STATUS_CHOICES)
    project_status = models.CharField(max_length=15, blank=False)
    picture = models.ImageField(upload_to='projects', blank=True)

    def __str__(self):
        return self.name