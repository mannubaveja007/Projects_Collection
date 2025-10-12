#scrap name of the project
"""To save the data to a JSON file, you can run your Scrapy spider with the following command:

scrapy crawl scrap -o products.json"""

import scrapy

class ProductSpider(scrapy.Spider):
    name = "product_spider"
    start_urls = [
        'https://nobero.com/pages/men '  # Change to your target website
    ]

    def parse(self, response):
        for product in response.css('div.product-item'):
            yield {
                'name': product.css('h2.product-title::text').get(),
                'price': product.css('span.product-price::text').get(),
                'availability': product.css('span.availability::text').get(),
                'description': product.css('p.product-description::text').get(),
            }

        # Handle pagination if applicable
        next_page = response.css('a.next-page::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)