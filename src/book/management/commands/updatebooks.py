from django.core.management import BaseCommand

from book.extract_metadata import save_books


class Command(BaseCommand):
    help = 'Update book in database'

    def handle(self, *args, **options):
        save_books()
        self.stdout.write("Data created")