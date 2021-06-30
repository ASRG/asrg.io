from django.contrib import admin

from .models import Training


@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    pass
