# Generated by Django 2.1.15 on 2020-08-19 15:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0026_auto_20200819_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='foundation',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 8, 19, 15, 50, 20, 823414, tzinfo=utc)),
        ),
    ]