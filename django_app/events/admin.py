from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from events.models import Event


class EventResource(resources.ModelResource):
    class Meta:
        model = Event
        fields = (
            "id",
            "title",
            "status",
            "event_type",
            "mode",
            "location",
            "presenter_first_name",
            "presenter_last_name",
            "presenter_designation",
            "presenter_bio",
            "event_description",
            "event_address",
            "link",
            "timezone",
            "start_date",
            "start_time",
            "end_date",
            "end_time",
        )


class EventAdmin(ImportExportModelAdmin):
    list_display = ("title", "event_type", "location", "host", "status", "start_date")
    search_fields = (
        "title",
        "host",
        "presenter_first_name",
        "presenter_last_name",
        "presenter_company_name",
    )
    readonly_fields = (
        "added_by",
        "added_on",
    )
    exclude = ("presenter_picture", "presenter_company_logo")

    filter_horizontal = ()
    list_filter = ("status", "mode", "event_type")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "title",
                    "status",
                    "event_type",
                    "mode",
                    "location",
                    "host",
                ),
            },
        ),
        (
            "Presenter Details",
            {
                "fields": (
                    "presenter_first_name",
                    "presenter_last_name",
                    "pres_img",
                    "presenter_profile_url",
                    "presenter_company_name",
                    "pres_com_log",
                    "presenter_bio",
                    "presenter_designation",
                    "presenter_company_website",
                ),
            },
        ),
        (
            "Event Details",
            {
                "fields": (
                    "event_address",
                    "event_description",
                    "link",
                    "slides",
                    "timezone",
                    "start_date",
                    "start_time",
                    "end_date",
                    "end_time",
                ),
            },
        ),
        (
            "Meta Data",
            {
                "fields": (
                    "added_by",
                    "added_on",
                )
            },
        ),
    )
    resource_class = EventResource

    def save_model(self, request, obj, form, change):
        obj.added_by = request.user
        return super().save_model(request, obj, form, change)


admin.site.register(Event, EventAdmin)
