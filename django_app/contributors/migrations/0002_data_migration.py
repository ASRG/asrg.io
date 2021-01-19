from django.db import migrations, models


def migrate_data(apps, schema_editor):
    old_contributor_model = apps.get_model("website", "contributor")
    contributor_model = apps.get_model("contributors", "contributor")
    for contributor in old_contributor_model.objects.all():
        contributor_model.objects.create(
            name=contributor.name,
            position=contributor.position,
            linkedin=contributor.linkedin,
            github=contributor.github,
            img=contributor.img,
            image_thumbnail=contributor.image_thumbnail
        )


class Migration(migrations.Migration):

    dependencies = [
        ("contributors", "0001_initial"),
        ("website", "0004_jobposting_company_name")
    ]

    operations = [
        migrations.RunPython(migrate_data),
    ]
