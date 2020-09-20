from django.db import models


class Events(models.Model):
    title = models.CharField(max_length=80)
    presenter = models.CharField(max_length=120)
    present_date = models.DateTimeField()
    description = models.textField(black=True)
