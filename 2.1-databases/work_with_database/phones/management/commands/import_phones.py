import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from datetime import datetime
from django.utils.text import slugify

class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))
        for phone in phones:
            Phone(name=phone['name'],
                  image=phone['image'],
                  price=phone['price'],
                  release_date=datetime.strptime(phone['release_date'], '%Y-%m-%d').date(),
                  Ite_exists=bool(phone['Ite_exists']),
                  slug=slugify(phone['name'])).save()
