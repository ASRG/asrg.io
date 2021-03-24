import logging

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.contrib.auth import get_user_model, models


DEFAULT_PASSWORD = "password"


class Command(BaseCommand):
    help = "Create test users for development purposes."

    def add_arguments(self, parser):
        parser.add_argument(
            "-f",
            "--force",
            action="store_true",
            help="Skip safety checks and create users anyway",
        )

    def handle(self, *args, **options):
        if (
            settings.DATABASES["default"]["ENGINE"] != "django.db.backends.sqlite3"
            and not options["force"]
        ):
            raise CommandError(
                "Database backend is not sqlite3, this does not look like a LOCAL DEV DB. "
                "Use --force if you are sure"
            )

        print(f"Default password is: {DEFAULT_PASSWORD}")
        def_group, _ = models.Group.objects.get_or_create(name="Default.Permissions")

        u, _ = get_user_model().objects.get_or_create(username="admin")
        u.first_name = "Admin"
        u.last_name = "User"
        u.is_superuser = True
        u.is_staff = True
        u.is_active = True
        u.set_password(DEFAULT_PASSWORD)
        u.save()

        print("One admin user created with username: admin")

        u, _ = get_user_model().objects.get_or_create(username="user")
        u.first_name = "Normal"
        u.last_name = "User"
        u.is_superuser = False
        u.is_staff = True
        u.is_active = True
        u.set_password(DEFAULT_PASSWORD)
        u.save()

        print("One admin user created with username: user")
