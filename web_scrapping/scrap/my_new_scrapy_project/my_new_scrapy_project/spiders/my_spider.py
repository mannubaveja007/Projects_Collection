import scrapy


class MySpiderSpider(scrapy.Spider):
    name = "my_spider"
    allowed_domains = ["example.com"]
    start_urls = ["https://example.com"]

    def parse(self, response):
        pass
