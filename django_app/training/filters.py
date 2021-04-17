import django_filters
from django import forms

from .models import Training


class TrainingFilter(django_filters.FilterSet):
    class Meta:
        model = Training
        fields = [
            "company",
            "location",
        ]
