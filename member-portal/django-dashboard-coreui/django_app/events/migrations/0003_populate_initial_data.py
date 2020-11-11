import csv

from datetime import datetime
from django.db import migrations
from events.timezones import TIMEZONES as TIMEZONE_CHOICES

def add_initial_data(apps, schema_editor):
    status_reversed = {
        "Completed": 4,
        "Cancelled": 5,
        "Invited": 3,
        "Confirmed": 2,
        "In Plan": 1,
    }
    event = apps.get_model("events", "event")
    chapter = apps.get_model("authentication", "chapter")
    chp = chapter.objects.all().first()
    try:
        with open("./events/migrations/asrg_events.csv") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                    continue
                names = row["Presenter"].split(" ")
                if len(names) >= 2:
                    first_name = names[0] 
                    last_name = names[1]
                else:
                    first_name = names
                    last_name = ".placeholder"
                start_date = datetime.strptime(row["Start"], '%d-%b-%Y')
                end_date = datetime.strptime(row["End"], '%d-%b-%Y')
                event.objects.create(
                    title=row["Event"],
                    status=status_reversed.get(row["Status"], 4),
                    event_type=row["Type"],
                    host=row["Host"],
                    mode='Internal',
                    location=chp,
                    pres_img='',
                    presenter_first_name=first_name,
                    presenter_last_name=last_name,
                    presenter_designation=".placeholder",
                    presenter_profile_url="https://placeholder.com", 
                    presenter_bio=".placeholder",
                    presenter_company_name='placeholder',
                    event_description="placeholder",
                    presenter_company_website='https://placeholder.com',
                    event_address="placeholder",
                    link='https://placeholder.com',
                    pres_com_log='',
                    timezone=TIMEZONE_CHOICES[0],
                    start_date=start_date.date(),
                    start_time=start_date.time(),
                    end_date=end_date.date(),
                    end_time=end_date.time(),
                )
            
                 
    except FileNotFoundError:
        return

class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20201111_1452'),
    ]

    operations = [
        migrations.RunPython(add_initial_data),
    ]
