# Generated by Django 2.1.15 on 2020-10-04 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_auto_20200923_1527'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='gender',
        ),
        migrations.AlterField(
            model_name='user',
            name='occupational_status',
            field=models.CharField(choices=[('', 'Occupational Status'), ('Student', 'Student'), ('Undergraduate Student', 'Undergraduate Student'), ('Graduate Student', 'Graduate Student'), ('Engineer', 'Engineer'), ('Manager', 'Manager'), ('Executive', 'Executive Management')], default=('', 'Occupational Status'), max_length=50),
        ),
    ]
