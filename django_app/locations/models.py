from django.db import models


# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=150, blank=False)
    short_name = models.CharField(max_length=10, blank=False)
    description = models.TextField(max_length=200, blank=False)
    picture = models.ImageField(upload_to='locations', blank=True)
    city = models.CharField(max_length=150, blank=False)
    country = models.CharField(max_length=150, blank=False)
    lead = models.CharField(max_length=150, blank=False)

    def __str__(self):
        return self.name
   

