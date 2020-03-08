# -*- coding: utf-8 -*-

# sneaky
# author - Quentin Ducasse
# https://github.com/QDucasse
# quentin.ducasse@ensta-bretagne.org

from sneaky.crawler.spiders import BaseSpider
from sneaky.crawler import DTLRItem
from scrapy.crawler import CrawlerProcess

class DTLRSpider(BaseSpider):

    name = "DTLRSpider"
    allowded_domains = ["dtlr.com"]
    start_urls = ["https://www.dtlr.com/collections/men-footwear"]

    def __init__(self):

        base_url                = "dtlr.com"
        item                    = DTLRItem
        # XPATH
        pagination_path         = "//div[@class='pagination']/a/@href"
        products_path           = "//div[@class='product-content']"
        # CSS
        product_name_path       = "div.product-content h2.a::text"
        product_price_path      = "div.product-prices meta::attr(data-current-price)"
        product_disc_price_path = ""
        product_link_path       = "div.product-content h2.a::attr(href)"

        super().__init__(base_url, item, pagination_path,
                         products_path, product_name_path, product_price_path,
                         product_disc_price_path, product_link_path)

if __name__=="__main__":
    process = CrawlerProcess()
    process.crawl(DTLRSpider)
    process.start()
