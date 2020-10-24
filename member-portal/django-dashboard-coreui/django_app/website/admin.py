from django.contrib import admin

from .models import JobPosting,Contributor,Announcement 



# @admin.register(Events)
# class EventsAdmin(admin.ModelAdmin):
#     pass


@admin.register(JobPosting)
class JobPostingAdmin(admin.ModelAdmin):
    list_display = ['title', 'job_category', 'location', 'date_posted']
    list_display_links = ('title',)
    search_fields = ['title', 'job_category', 'location']
    list_filter = ('location', 'job_category')

admin.site.register(Contributor)

admin.site.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
	list_display = ['title', 'date_posted']
	list_filter = ['date_posted']