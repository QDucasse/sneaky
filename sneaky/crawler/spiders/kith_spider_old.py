# -*- coding: utf-8 -*-

# sneaky
# author - Quentin Ducasse
# https://github.com/QDucasse
# quentin.ducasse@ensta-bretagne.org

from sneaky.crawler import KithItem

from scrapy         import Spider
from scrapy.http    import Request
from scrapy.crawler import CrawlerProcess

class KithSpider(Spider):

    name = "KithSpiderOld"
    start_urls = ["https://kith.com/collections/mens-footwear"]

    def parse(self, response):
        next_page_url = response.xpath("//div[@class='pagination']/a/@href")
        for item in self.scrape(response):
            yield item
        if next_page_url:
            path = next_page_url.extract_first()
            next_page = response.urljoin(path)
            print("Found url: {}".format(next_page))
            yield Request(next_page, callback=self.parse)

    def scrape(self,response):
        # products = response.css('div.product-card')
        products = response.xpath("//div[@class='product-card']")
        for product in products:
            item = KithItem()
            item['name']  = product.css('div.product-card__information h1.product-card__title::text').get().strip()
            item['price'] = product.css('div.product-card__information span.product-card__price::text').get().strip()

            # If the item is on discount
            if item['price'] == '':
                item['price'] = product.css('div.product-card__information span.product-card__price::text').extract()[1].strip()
            item['link']  = 'kith.com' + product.css('div.product-card__image-slide-container a.product-card__image-slide::attr(href)').get().strip()
            # item['name']  = product.xpath("//div[@class='product-card__information']/h1[contains(@class,'product-card__title')]/text()").get().strip()
            # item['price']  = product.xpath("//div[@class='product-card__information']/span[contains(@class,'product-card__price')]/text()").get().strip()
            # item['link']  = 'kith.com' + product.xpath("//a[contains(@class,'product-card__image-slide')]/@href").get().strip()
            yield item

        # yield Request(KithURL, callback=self.parse, dont_filter=True, priority=0)

if __name__ == "__main__":

    # CRAWLER SETTINGS
    # crawler_settings = Settings()
    # crawler_settings.setmodule(settings)
    # process = CrawlerProcess(settings=crawler_settings)

    process = CrawlerProcess()
    process.crawl(KithSpider)
    process.start()
