# Generated by Django 2.1.15 on 2020-12-21 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0010_auto_20201220_0652'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chapter',
            name='description',
        ),
        migrations.RemoveField(
            model_name='chapter',
            name='meetup_link',
        ),
        migrations.RemoveField(
            model_name='chapter',
            name='picture',
        ),
    ]
