from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "List all users in the database"

    def handle(self, *args, **options):
        print("all users command executed")
        users = User.objects.all()
        for user in users:
            self.stdout.write(
                self.style.SUCCESS(f"Username: {user.username}, Email: {user.email}")
            )
