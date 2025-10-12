#scrap name of the project
#product_api for django
"""To save the data to a JSON file, you can run your Scrapy spider with the following command:

scrapy crawl product_spider -o products.json
Now, set up a ReactJS frontend to display the product data.

Initialize React Project
Create a React project:

npx create-react-app product_frontend

"""
import scrapy
import json

class noberoSpider(scrapy.Spider):
    name = 'nobero_spider' #define name

    def start_requests(self):
        urls = [
            "https://nobero.com/collections/men-oversized-t-shirts",
            "https://nobero.com/products/lunar-echo-oversized-t-shirt-1?variant=45663963218086",
            "https://nobero.com/products/less-scrolling-oversized-t-shirt?variant=44791975411878",
        ] #urls to scrap
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse) # start sending request to these urls

    def parse(self, response):
        # Extract all <script> tags with type "application/ld+json"
        scripts = response.xpath('//script[@type="application/ld+json"]/text()').getall()

        for script in scripts:
            # Load JSON data
            try:
                json_data = json.loads(script)
            except json.JSONDecodeError:
                continue  # Skip if it is not valid json

            # Check if this json data is a list or a single object
            if isinstance(json_data, dict):
                data_item = {
                    'name': json_data.get('name'),
                    'url': json_data.get('url'),
                    'image': json_data.get('image'),
                    'description': json_data.get('description'),
                    'price': json_data.get('offers', {}).get('price'),
                    'priceCurrency': json_data.get('offers', {}).get('priceCurrency'),
                    'availability': json_data.get('offers', {}).get('availability'),
                }
                # Filter data where none of the fields are None
                if self.is_valid_data(data_item):
                    yield data_item
            elif isinstance(json_data, list):
                for item in json_data:
                    data_item = {
                        'name': item.get('name'),
                        'url': item.get('url'),
                        'image': item.get('image'),
                        'description': item.get('description'),
                        'price': item.get('offers', {}).get('price'),
                        'priceCurrency': item.get('offers', {}).get('priceCurrency'),
                        'availability': item.get('offers', {}).get('availability')[-2],
                    }
                    # Filter data where none of the fields are None
                    if self.is_valid_data(data_item):
                        yield data_item

    def is_valid_data(self, data_item):
        """
        Check if the data item contains no null values.
        """
        return all(value is not None for key, value in data_item.items() if key != "id")


#scrapy crawl product_spider
# scrapy crawl nobero_spider -o output1.json