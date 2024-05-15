from django.core.management.base import BaseCommand

# from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "List all users in the database"

    def handle(self, *args, **options):
        print("creating admin user")
        # Create a superuser
