# Generated by Django 2.1.15 on 2020-11-06 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('short_name', models.CharField(max_length=6)),
                ('view_status', models.CharField(choices=[('Public', 'Public'), ('Private', 'Private')], max_length=20)),
                ('project_status', models.CharField(max_length=15)),
                ('picture', models.ImageField(blank=True, upload_to='projects')),
            ],
        ),
    ]
