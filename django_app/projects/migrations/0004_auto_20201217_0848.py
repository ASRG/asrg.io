# Generated by Django 2.1.15 on 2020-12-17 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20201112_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_status',
            field=models.CharField(choices=[('Status: Planning Phase', 'Status: Planning Phase'), ('Status: In Progress', 'Status: In Progress'), ('Status: Completed', 'Status: Completed')], max_length=50),
        ),
    ]
