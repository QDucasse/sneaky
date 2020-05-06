# -*- coding: utf-8 -*-

# sneaky
# author - Quentin Ducasse
# https://github.com/QDucasse
# quentin.ducasse@ensta-bretagne.org

from sneaky.crawler.spiders import BaseSpider
from sneaky.crawler import FootshopItem
from scrapy.crawler import CrawlerProcess

class FootshopSpider(BaseSpider):

    name = "FootshopSpider"
    allowded_domains = ["footshop.com"]
    start_urls = ["https://www.footshop.com/en/5-mens-shoes/location-available_online"]

    def __init__(self):

        base_url                = "footshop.com"
        item                    = FootshopItem
        # XPATH
        pagination_path         = "//*[starts-with(@class,\"PaginationLinks_nav\")]/a/@href"
        products_path           = "//*[starts-with(@class,\"Products_product\")]"
        product_name_path       = "//*[starts-with(@class,\"Product_name\")]/@title"
        product_price_path      = "//*[starts-with(@class,\"ProductPrice_price\")]/strong/text()"
        product_disc_price_path = "//*[starts-with(@class,\"ProductPrice_price\")]/strong/text()"
        product_link_path       = "//a[starts-with(@class,\"Product_text\")]/@href"

        super().__init__(base_url, item, pagination_path,
                         products_path, product_name_path, product_price_path,
                         product_disc_price_path, product_link_path)

if __name__=="__main__":
    process = CrawlerProcess()
    process.crawl(FootshopSpider)
    process.start()
