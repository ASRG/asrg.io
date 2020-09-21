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
                'presenter_company_name',
                'presenter_company_logo',
                'presenter_bio',
            ),
        }),

        ('Event Details', {
            'fields': (
                'event_address',
                'link',
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


admin.site.register(Event, EventAdmin)
