import logging

from django.core.management.base import BaseCommand, CommandError

from account.models import User

logger = logging.getLogger('views')


class Command(BaseCommand):
    """Creates Superuser"""

    def handle(self, *args, **options):
        users = [
            User(
                username=f'user_{i}', password=f'password{i}'
            ) for i in range(10)
        ]
        User.objects.bulk_create(users)
        logger.debug('Congratulations, 10 users is created!')

