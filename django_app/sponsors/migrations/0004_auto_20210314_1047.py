# Generated by Django 2.2.19 on 2021-03-14 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0003_auto_20210310_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
