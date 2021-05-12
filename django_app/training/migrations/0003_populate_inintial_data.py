import csv

from datetime import datetime
from django.db import migrations


def add_initial_data(apps, schema_editor):
    training = apps.get_model("training", "training")
    try:
        with open("./training/migrations/asrg_trainings.csv") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                training.objects.create(
                    company=row["Company"],
                    title=row["Title"],
                    description=row["Description"],
                    costs=row["Costs"],
                    currency=row["Currency"],
                    duration=row["Duration"],
                    location=row["Location"],
                    link=row["Link"],
                )

    except FileNotFoundError:
        return


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0002_auto_20210512_1608'),
    ]

    operations = [
        migrations.RunPython(add_initial_data),
    ]
