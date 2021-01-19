import django_filters
from django import forms

from website.models import JobPosting


class JobPostingFilters(django_filters.FilterSet):
    location_choices = ((None, None),)
    job_category_choices = ((None, None),)

    def __init__(self, *args, **kwargs):
        super(JobPostingFilters, self).__init__(*args, **kwargs)
        location_choices = list(
            (x, x) for x in self.queryset.order_by('location').values_list('location', flat=True).distinct()
        )
        job_category_choices = list(
            (x, x) for x in self.queryset.order_by('job_category').values_list('job_category', flat=True).distinct()
        )
        self.filters['location'].field.choices = location_choices
        self.filters['job_category'].field.choices = job_category_choices

    location = django_filters.MultipleChoiceFilter(
        choices=location_choices, widget=forms.Select(attrs={'class': 'form-control'})
    )
    job_category = django_filters.MultipleChoiceFilter(
        choices=location_choices, widget=forms.Select(attrs={'class': 'form-control'})
    )
    date_posted = django_filters.DateRangeFilter(field_name='date_posted')

    class Meta:
        model = JobPosting
        fields = ['job_category', 'location', 'date_posted']
