import json
import os
from django.core.management.base import BaseCommand
from products.models import Product

import json
from django.core.management.base import BaseCommand
from products.models import Product


class Command(BaseCommand):
    help = 'Load products from a JSON file'

    def add_arguments(self, parser):
        # Add an argument to accept the JSON file path
        parser.add_argument('file_path', type=str, help='Path to the JSON file containing product data')

    def handle(self, *args, **options):
        file_path = options['file_path']

        # Open the JSON file and load data
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                # Process data and save to the database
                for item in data:
                    # Example saving to database
                    Product.objects.create(
                        name=item.get('name'),
                        url=item.get('url'),
                        image=item.get('image'),
                        description=item.get('description'),
                        price=item.get('price'),
                        price_currency=item.get('priceCurrency'),
                        availability=item.get('availability')
                    )
            self.stdout.write(self.style.SUCCESS('Successfully loaded products'))
        except json.JSONDecodeError as e:
            self.stdout.write(self.style.ERROR(f'Error loading JSON: {e}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'An error occurred: {e}'))
# python manage.py load_products D:\intern\web_scrapping\scrap\my_new_scrapy_project\my_new_scrapy_project\spiders\output1.json
