# Generated by Django 2.1.15 on 2020-08-19 00:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0015_auto_20200819_0608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='foundation',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 8, 19, 0, 39, 9, 36222, tzinfo=utc)),
        ),
    ]