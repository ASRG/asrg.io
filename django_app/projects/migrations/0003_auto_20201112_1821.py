# Generated by Django 2.1.15 on 2020-11-12 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20201112_1810'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='picture',
            new_name='project_picture',
        ),
    ]
