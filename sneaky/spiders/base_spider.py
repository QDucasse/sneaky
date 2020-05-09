# -*- coding: utf-8 -*-

# sneaky
# author - Quentin Ducasse
# https://github.com/QDucasse
# quentin.ducasse@ensta-bretagne.org
from abc import abstractmethod, ABC
import unicodedata

from sneaky import BaseItem

from scrapy         import Spider
from scrapy.http    import Request
from scrapy.crawler import CrawlerProcess

class BaseSpider(Spider):

    def __init__(self,base_url, item, pagination,
                 products, product_name, product_price, product_link):

        self.base_url           = base_url
        self.pagination_path    = pagination
        self.products_path      = products
        self.product_name_path  = product_name
        self.product_price_path = product_price
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
            next_page = self.handle_next_page(response,next_page_url)
            print("Found url: {}".format(next_page))
            yield Request(next_page, callback=self.parse)

    def scrape(self,response):
        # Looks for the products
        products = response.xpath(self.products_path)

        # For each one of the products, the name, price and link is extracted
        for product in products:
            item = BaseItem()
            item['name']  = product.xpath(self.product_name_path).get().strip()
            scrapped_price = product.xpath(self.product_price_path).get().strip()
            item['price'] = self.handle_price(scrapped_price)
            scrapped_link = product.xpath(self.product_link_path).get().strip()
            item['link']  = self.handle_link(scrapped_link)
            yield item

    @abstractmethod
    def handle_next_page(self,response,scrapped_url):
        pass

    @abstractmethod
    def handle_link(self,scrapped_link):
        pass

    def handle_price(self,scrapped_price):
        return unicodedata.normalize("NFKD", scrapped_price)
