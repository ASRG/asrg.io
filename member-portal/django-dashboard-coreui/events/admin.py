from django.contrib import admin

from events.models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_type', 'location', 'host', 'status',)
    search_fields = ('title', 'host', 'presenter_first_name', 'presenter_last_name', 'presenter_company_name',)
    readonly_fields = ('added_by', 'added_on',)

    filter_horizontal = ()
    list_filter = ('status', 'mode','event_type')
    fieldsets = (
        (None, {
            'fields': (
                'title',
                'status',
                'event_type',
                'mode',
                'location',
                'host',
            ),
        }),

        ('Presenter Details', {
            'fields': (
                'presenter_first_name',
                'presenter_last_name',
                'presenter_picture',
                'presenter_profile_url',
                'presenter_company_name',
                'presenter_company_logo',
                'presenter_bio',
                'presenter_designation',
                'presenter_company_website',
            ),
        }),

        ('Event Details', {
            'fields': (
                'event_address',
                'event_description',
                'link',
                'timezone',
                'start_date',
                'start_time',
                'end_date',
                'end_time',
            ),
        }),

        ('Meta Data', {
            'fields': (
                'added_by',
                'added_on',
            )
        })
    )

    def save_model(self, request, obj, form, change):
        obj.added_by = request.user
        return super().save_model(request, obj, form, change)


admin.site.register(Event, EventAdmin)
