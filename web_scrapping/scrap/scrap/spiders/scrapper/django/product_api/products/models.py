from django.db import models

# Create your models here.

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField(null=True, blank=True)  # Make sure this field exists
    image = models.URLField(null=True, blank=True)  # Ensure this field exists
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price_currency = models.CharField(max_length=10, null=True, blank=True)  # Ensure this field exists
    availability = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

# python manage.py load_products D:\intern\web_scrapping\scrap\my_new_scrapy_project\my_new_scrapy_project\spiders\output1.json
