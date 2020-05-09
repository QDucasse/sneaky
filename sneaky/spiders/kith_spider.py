# -*- coding: utf-8 -*-

# sneaky
# author - Quentin Ducasse
# https://github.com/QDucasse
# quentin.ducasse@ensta-bretagne.org

from scrapy.crawler import CrawlerProcess

from sneaky.spiders import BaseSpider
from sneaky         import KithItem


class KithSpider(BaseSpider):

    name = "kith"
    allowded_domains = ["kith.com"]
    start_urls = ["https://kith.com/collections/mens-footwear"]

    def __init__(self):
        base_url                = "kith.com"
        item                    = KithItem
        # XPATH
        pagination_path         = "//div[@class='pagination']/a/@href"
        products_path           = "//div[@class='product-card']"
        product_name_path       = ".//h1[@class='product-card__title']/text()"
        product_price_path      = ".//span[@class='product-card__price']/text()"
        product_link_path       = ".//a[@class='product-card__link']/@href"

        super().__init__(base_url, item, pagination_path,
                         products_path, product_name_path,
                         product_price_path, product_link_path)

    def handle_link(self,scrapped_link):
        return self.base_url + scrapped_link

    def handle_next_page(self,response,scrapped_url):
        path = scrapped_url.extract_first()
        next_page = response.urljoin(path)
        return next_page

if __name__=="__main__":
    process = CrawlerProcess()
    process.crawl(KithSpider)
    process.start()
