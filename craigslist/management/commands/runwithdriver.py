from globals import get_global_driver
from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = 'creates driver before running server'

    def handle(self, *args, **options):
        driver = get_global_driver(start_url='https://www.craigslist.org/about/sites#US', args=["--headless"])
        call_command('runserver')

