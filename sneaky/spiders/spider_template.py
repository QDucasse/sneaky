# -*- coding: utf-8 -*-

# sneaky
# author - Quentin Ducasse
# https://github.com/QDucasse
# quentin.ducasse@ensta-bretagne.org
from scrapy.crawler import CrawlerProcess

from sneaky.spiders import BaseSpider
from sneaky import BaseItem

class NAMESpider(BaseSpider):

    name = "NAMESpider"
    allowded_domains = ["NAME.com"]
    start_urls = ["URL"]

    def __init__(self):

        base_url                = "NAME.com"
        item                    = NAMEItem
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
