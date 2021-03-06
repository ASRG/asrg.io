from django.contrib import admin

from .models import JobPosting


@admin.register(JobPosting)
class JobPostingAdmin(admin.ModelAdmin):
    list_display = ['title', 'job_category', 'location', 'date_posted']
    list_display_links = ('title',)
    # search_fields = ['title', 'job_category', 'location']
    # list_filter = ('location', 'job_category')
