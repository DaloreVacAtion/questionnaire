import logging

from django.core.management.base import BaseCommand, CommandError

from account.models import User

logger = logging.getLogger('views')


class Command(BaseCommand):
    """Creates Superuser"""
    help = 'Create admin if it does not exist'

    def handle(self, *args, **options):
        admin = User.objects.create_superuser(username='admin', password='Tr0ub4dor@3')
        admin.is_active = True
        admin.is_admin = True
        admin.save()
        logger.debug('Congratulations, Admin Account is created!')
