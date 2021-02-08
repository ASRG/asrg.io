from django.db import migrations, models


def migrate_data(apps, schema_editor):
    old_announcement_model = apps.get_model("website", "announcement")
    announcement_model = apps.get_model("announcements", "announcement")
    for announcement in old_announcement_model.objects.all():
        announcement_model.objects.create(
           title=announcement.title,
           announcement=announcement.announcement,
           date_posted=announcement.date_posted
        )


class Migration(migrations.Migration):

    dependencies = [
        ("announcements", "0001_initial"),
        ("website", "0004_jobposting_company_name")
    ]

    operations = [
        migrations.RunPython(migrate_data),
    ]
