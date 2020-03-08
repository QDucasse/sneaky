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
        pagination_path         = ""
        products_path           = ""
        # CSS
        product_name_path       = ""
        product_price_path      = ""
        product_disc_price_path = ""
        product_link_path       = ""

        super().__init__(base_url, item, pagination_path,
                         products_path, product_name_path, product_price_path,
                         product_disc_price_path, product_link_path)

if __name__=="__main__":
    process = CrawlerProcess()
    process.crawl(NAMESpider)
    process.start()
