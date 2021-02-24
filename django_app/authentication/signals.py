from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save
from django.contrib.auth.models import Group, Permission
from django.conf import settings
from django.dispatch import receiver

from authentication.models import Chapter, User


@receiver(post_save, sender=Chapter)
def add_groups_asrgs(sender, instance, created, **kwargs):
    if created:
        location = instance.location
        ct = ContentType.objects.get(app_label="authentication", model="chapter")

        # Create permissions needed for the new chapter
        asrg_perm, _ = Permission.objects.get_or_create(
            codename=location, name=location, content_type=ct
        )
        local_lead_perm, _ = Permission.objects.get_or_create(
            codename=f"local-lead-{location}",
            name=f"Local lead {location}",
            content_type=ct,
        )

        # Add groups for the new chapters that will be used to granualarly add permissions
        asrg_goup, _ = Group.objects.get_or_create(name=location)
        asrg_goup.permissions.add(asrg_perm)
        local_lead_group, _ = Group.objects.get_or_create(name=f"local-lead-{location}")
        local_lead_group.permissions.add(local_lead_perm)
