# Generated by Django 2.2.20 on 2021-04-13 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0017_auto_20210303_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='description',
            field=models.TextField(),
        ),
    ]
