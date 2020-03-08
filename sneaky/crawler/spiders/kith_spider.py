# -*- coding: utf-8 -*-

# sneaky
# author - Quentin Ducasse
# https://github.com/QDucasse
# quentin.ducasse@ensta-bretagne.org

from sneaky.crawler.spiders import BaseSpider
from sneaky.crawler import KithItem
from scrapy.crawler import CrawlerProcess

class KithSpider2(BaseSpider):

    name = "KithSpider"
    allowded_domains = ["kith.com"]
    start_urls = ["https://kith.com/collections/mens-footwear"]

    def __init__(self):
        base_url           = "kith.com"
        pagination_path    = "//div[@class='pagination']/a/@href"
        products_path      = "//div[@class='product-card']"
        product_name_path  = "div.product-card__information h1.product-card__title::text"
        product_price_path = "div.product-card__information span.product-card__price::text"
        product_disc_price_path = "div.product-card__information span.product-card__price::text"
        product_link_path  = "div.product-card__image-slide-container a.product-card__image-slide::attr(href)"
        item = KithItem
        super().__init__(base_url,pagination_path,item,products_path,product_name_path,product_price_path,product_disc_price_path,product_link_path)


if __name__=="__main__":
    process = CrawlerProcess()
    process.crawl(KithSpider2)
    process.start()
