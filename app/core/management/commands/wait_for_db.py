"""
django command to wait for the database to be available.
"""

from django.core.management.base import BaseCommand
import time

class Command(BaseCommand):
    """Django command to wait for the database to be available."""

    def handle(self, *args, **options):
        self.stdout.write('Waiting for database...')
        db_up = False
        while not db_up:
            try:
                # Try to get a cursor to check if the database is up
                from django.db import connections
                connections['default'].cursor()
                db_up = True
            except Exception:
                self.stdout.write('Database unavailable, waiting 1 second...')
                
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available!'))