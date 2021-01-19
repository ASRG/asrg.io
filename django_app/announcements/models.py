from django.db import models


class Announcement(models.Model):
    title = models.CharField(max_length=100)
    announcement = models.TextField(max_length=300)
    date_posted = models.DateTimeField(blank=True, auto_now_add=True)

    def __str__(self):
        return self.title
