from django.contrib import admin

from .models import Training


@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "link")
    search_fields = ("title",)
    list_filter = ("status",)
