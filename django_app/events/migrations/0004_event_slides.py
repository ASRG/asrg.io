# Generated by Django 2.2.20 on 2021-04-13 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_populate_initial_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='slides',
            field=models.FileField(blank=True, null=True, upload_to='slides/'),
        ),
    ]