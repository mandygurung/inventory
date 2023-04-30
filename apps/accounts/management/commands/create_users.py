from typing import Any, Optional
from django.core.management.base import BaseCommand, CommandParser
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string

User = get_user_model()

class Command(BaseCommand):

    help = 'Create dummy users.'

    def add_arguments(self, parser: CommandParser) -> None:
        
        parser.add_argument("total", type=int, help="Indicates the total number of users to be created.")

    def handle(self, *args: Any, **options: Any) -> str | None:

        total = options["total"]

        for _ in range(total):
            User.objects.create(
                username=get_random_string(),
                email = "",
                password="123"
            )

        self.stdout.write(f"{total} user's created successfully.")