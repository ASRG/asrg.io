# Generated by Django 2.1.15 on 2020-11-13 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_auto_20201110_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='chapter',
            field=models.ManyToManyField(blank=True, null=True, related_name='users', to='authentication.Chapter'),
        ),
    ]
