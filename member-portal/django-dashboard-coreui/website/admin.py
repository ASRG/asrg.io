from django.contrib import admin

from .models import Events


@admin.register(Event)
class EventsAdmin(admin.ModelAdmin):
    list_display = ['event_status', 'present_date', 'title', 'presenter']


@admin.register(Project)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['project_status', 'project_name', 'project_lead']
