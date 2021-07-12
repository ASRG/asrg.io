# Generated by Django 2.2.20 on 2021-05-17 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0004_merge_20210517_0838'),
    ]

    operations = [
        migrations.AddField(
            model_name='training',
            name='status',
            field=models.CharField(choices=[('Submitted', 'Submitted'), ('Released', 'Released'), ('Expired', 'Expired')], default='Submitted', max_length=150),
        ),
        migrations.AlterField(
            model_name='training',
            name='link',
            field=models.URLField(blank=True),
        ),
    ]