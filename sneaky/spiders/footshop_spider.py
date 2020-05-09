# -*- coding: utf-8 -*-

# sneaky
# author - Quentin Ducasse
# https://github.com/QDucasse
# quentin.ducasse@ensta-bretagne.org
from scrapy.crawler import CrawlerProcess

from sneaky.spiders import BaseSpider
from sneaky import FootshopItem


class FootshopSpider(BaseSpider):

    name = "footshop"
    allowded_domains = ["footshop.com"]
    start_urls = ["https://www.footshop.com/en/5-mens-shoes/location-available_online"]

    def __init__(self):
        base_url                = "footshop.com"
        item                    = FootshopItem
        # XPATH
        pagination_path         = "(//a[starts-with(@class,\"PaginationLink_item\")]/@href)[last()]"
        products_path           = "//*[starts-with(@class,\"Products_product\")]"
        product_name_path       = ".//*[starts-with(@class,\"Product_name\")]/@title"
        product_price_path      = ".//*[starts-with(@class,\"ProductPrice_price\")]/strong/text()"
        product_link_path       = ".//a[starts-with(@class,\"Product_text\")]/@href"

        super().__init__(base_url, item, pagination_path,
                         products_path, product_name_path,
                         product_price_path, product_link_path)

    def handle_link(self,scrapped_link):
        return scrapped_link

    def handle_next_page(self,response,scrapped_url):
        path = scrapped_url.extract_first()
        total_path = "orderby-activated_at/orderway-desc/" + path[1:]
        next_page = response.urljoin(total_path)
        return next_page


if __name__=="__main__":
    process = CrawlerProcess()
    process.crawl(FootshopSpider)
    process.start()
