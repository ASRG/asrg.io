# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""
import base64

from django.contrib import admin, messages
from django.utils import timezone
from django.utils.encoding import force_bytes
from django.contrib.auth.models import Permission
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.sites.shortcuts import get_current_site
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.core.signing import TimestampSigner
from django.contrib.auth.tokens import default_token_generator
from django.core import mail
from django.conf import settings
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from authentication.models import Chapter, User, UserProfile


class ChapterInLine(admin.StackedInline):
    model = User.chapter.through
    extra = 0
    show_change_link = True


@admin.register(User)
class UserAdmin(AuthUserAdmin):
    list_display = ("first_name", "last_name", "country", "date_joined", "last_login")
    search_fields = ("country", "first_name", "last_name")
    inlines = [ChapterInLine]
    readonly_fields = ("date_joined", "last_login")
    actions = ["send_registration_mail"]

    def send_registration_mail(self, request, queryset):
        current_site = get_current_site(request)
        _user_failed = ""
        success = True
        mail_subject = "Activate your account."
        for user in queryset:
            message = render_to_string(
                "authentication/email/acc_activate_email.html",
                {
                    "user": user.username,
                    "domain": current_site.domain,
                    "uid": base64.urlsafe_b64encode(force_bytes(user.pk)).decode(
                        "utf-8"
                    ),
                    "token": TimestampSigner().sign(
                        default_token_generator.make_token(user)
                    ),
                },
            )
            plain_message = strip_tags(message)
            to_email = user.email
            if (
                mail.send_mail(
                    mail_subject,
                    plain_message,
                    settings.EMAIL_HOST_USER,
                    [to_email],
                    html_message=message,
                )
                == 0
            ):
                success = False
                _user_failed += f"{user.username}, "
            user.verification_email_sent_date = timezone.now()
        if success:
            self.message_user(
                request,
                "E-mail was send successfully for all user(s)",
                messages.SUCCESS,
            )
        else:
            self.message_user(
                request,
                f"Send the e-mail failed for the following user(s): {_user_failed}",
                messages.ERROR,
            )

    send_registration_mail.short_description = "Send activation E-mail to user(s)"

    def save_model(self, request, obj, form, change):
        # add chapter permissions if chapter is changed -- need to save for all perms
        obj.save()
        if obj.chapter:
            for chapter in obj.chapter.all():
                perm = Permission.objects.get(codename=chapter)
                print(perm)
                obj.user_permissions.add(perm)

        return super(UserAdmin, self).save_model(request, obj, form, change)


class ChapterResource(resources.ModelResource):
    class Meta:
        model = Chapter
        fields = (
            "id",
            "location",
            "city",
            "country",
            "lead",
            "foundation",
            "latitude",
            "longitude",
            "description",
            "meetup_link",
            "picture_src",
            "picture",
            "email",
        )


@admin.register(Chapter)
class ChapterAdmin(ImportExportModelAdmin):
    list_display = ["location", "city", "country", "lead", "foundation", "age"]
    list_filter = ("city", "country")
    readonly_fields = ["age"]
    resource_class = ChapterResource

    def age(self, obj):
        now = timezone.now()
        delta = now - obj.foundation
        fraction = delta.days / 365.25
        return f"{fraction:.2f}"


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("username", "dob", "gender", "field_of_study")
    search_fields = ("username", "field_of_study")
    readonly_fields = ("date_joined", "last_login")

    filter_horizontal = ()
    fieldsets = ()

    def username(self, obj):
        return obj.user.username
