from django.db import migrations, models


def migrate_data(apps, schema_editor):
    old_job_model = apps.get_model("website", "jobpostings")
    job_model = apps.get_model("job", "jobpostings")
    for job in old_job_model.objects.all():
        job_model.objects.create(
            title=job.title,
            job_category=job.job_category,
            location=job.location,
            date_posted=job.date_posted,
            job_description=job.job_description,
            job_link=job.job_link,
            company_name=job.company_name,
        )


class Migration(migrations.Migration):

    dependencies = [("job", "0001_initial"), ("website", "0004_jobposting_company_name")]

    operations = [
        migrations.RunPython(migrate_data),
    ]
