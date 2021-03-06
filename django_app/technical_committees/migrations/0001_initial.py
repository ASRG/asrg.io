from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Technical_committee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('short_name', models.CharField(max_length=6)),
                ('view_status', models.CharField(choices=[('Public', 'Public'), ('Private', 'Private')], max_length=20)),
                ('tc_status', models.CharField(max_length=15)),
                ('picture', models.ImageField(blank=True, upload_to='technical-committee')),
            ],
        ),
    ]
