from csv import DictReader
from datetime import datetime

from django.core.management import BaseCommand

from .models import Events
from pytz import UTC


DATETIME_FORMAT = '%d.%m.%Y'

ALREADY_LOADED_ERROR_MESSAGE = ""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from events.csv"

    def handle(self, *args, **options):
        if Events.objects.exists():
            print('Event data already loaded...exiting.')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return

        print("Loading event data...")
        for row in DictReader(open('ASRG_Roadmap.csv')):
            event = Events()
            event.title = row['Event']
            event.presenter = row['Presenter']
            event.location = row['ASRG']
            event.presenter_company = row['Organization']
            event.event_status = row['Status']
            event.present_date = row['Start']
            event.save()

        print("Data Imported.")
