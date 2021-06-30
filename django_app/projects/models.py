from django.db import models

# Create your models here.


PROJECT_STATUS_CHOICES = (
    ('Status: Planning Phase', 'Status: Planning Phase'),
    ('Status: In Progress', 'Status: In Progress'),
    ('Status: Completed', 'Status: Completed'),
)
class Project(models.Model):
    name = models.CharField(max_length=150, blank=False)
    description = models.TextField(blank=False)
    short_name = models.CharField(max_length=6, blank=False)
    project_status = models.CharField(max_length=50, choices=PROJECT_STATUS_CHOICES)
    project_picture = models.ImageField(upload_to='projects', blank=True)

    def __str__(self):
        return self.name