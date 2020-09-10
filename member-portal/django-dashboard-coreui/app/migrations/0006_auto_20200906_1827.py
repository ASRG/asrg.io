# Generated by Django 2.1.15 on 2020-09-06 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_userprofile_chapter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(blank=True, default=' ', null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='dob',
            field=models.DateField(blank=True, null=True, verbose_name='Date of Birth'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='field_of_study',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Prefer Not To Say', 'Prefer Not to Say')], max_length=17),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='occupational_status',
            field=models.CharField(choices=[('student', 'Student'), ('undergraduate student', 'Undergraduate Student'), ('graduate student', 'Graduate Student'), ('professional', 'Professional')], max_length=25),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(default='def.jpg', upload_to='profile pictures'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='skills',
            field=models.CharField(blank=True, default=' ', max_length=350, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='status',
            field=models.CharField(blank=True, default=' ', max_length=256, null=True),
        ),
    ]
