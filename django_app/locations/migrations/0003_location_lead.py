# Generated by Django 2.1.15 on 2020-11-12 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_auto_20201112_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='lead',
            field=models.CharField(default='DEFAULT VALUE', max_length=150),
        ),
    ]
