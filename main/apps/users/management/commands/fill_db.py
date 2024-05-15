from django.core.management.base import BaseCommand
from tests.db import fill_db


class Command(BaseCommand):
    help = "Command to fill the developers database with some initial data"

    def handle(self, *args, **options):
        print("fill_db command started")
        try:
            fill_db()
        except Exception as e:
            print(f"Error: {e}")
        print("fill_db command executed")
