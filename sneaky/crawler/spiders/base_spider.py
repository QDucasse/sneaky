# -*- coding: utf-8 -*-

# sneaky
# author - Quentin Ducasse
# https://github.com/QDucasse
# quentin.ducasse@ensta-bretagne.org

from sneaky.crawler import BaseItem

from scrapy         import Spider
from scrapy.http    import Request
from scrapy.crawler import CrawlerProcess

class BaseSpider(Spider):

    # name = "TO_BE_GIVEN"
    # allowded_domains = ["TO_BE_GIVEN"]
    # start_urls = [TO_BE_GIVEN]

    def __init__(self,base_url, item, pagination,
                 products, product_name, product_price, product_disc_price, product_link):

        self.base_url           = base_url
        self.pagination_path    = pagination
        self.products_path      = products
        self.product_name_path  = product_name
        self.product_price_path = product_price
        self.product_disc_price_path = product_disc_price
        self.product_link_path  = product_link
        self.item = item

    def parse(self, response):
        # Scrape the items in the response
        for item in self.scrape(response):
            yield item

        # Scrape the next page url
        next_page_url = response.xpath(self.pagination_path)
        # If the url of the next page is found, it is concatenated to the base
        # one, displayed then fed as a new Request to the crawler
        if next_page_url:
            path = next_page_url.extract_first()
            next_page = response.urljoin(path)
            print("Found url: {}".format(next_page))
            yield Request(next_page, callback=self.parse)

    def scrape(self,response):
        # Looks for the products
        products = response.xpath(self.products_path)

        # For each one of the products, the name, price and link is extracted
        for product in products:
            item = BaseItem()
            item['name']  = product.xpath(self.product_name_path).get().strip()
            item['price'] = product.xpath(self.product_price_path).get().strip()
            if item['price'] == '':
                item['price'] = product.xpath(self.product_disc_price_path).get().strip()
            item['link']  = self.base_url + product.xpath(self.product_link_path).get().strip()
            yield item

if __name__=="__main__":
    process = CrawlerProcess()
    process.crawl(BaseSpider)
    process.start()
