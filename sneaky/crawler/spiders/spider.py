# -*- coding: utf-8 -*-

# sneaky
# author - Quentin Ducasse
# https://github.com/QDucasse
# quentin.ducasse@ensta-bretagne.org

import scrapy

KithURL = "https://kith.com/collections/mens-footwear"

class KithSpider(scrapy.Spider):

    name = "KithSpider"
    # allowded_domains = ["kith.com"]
    start_urls = [KithURL]

    def parse(self, response):
        # products = Selector(response).xpath('//div[@class="product-card"]')

        for product in response.css('div.product-card'):
            # item = KithItem()
            # item['name'] = product.xpath('div/div/a[1]/img/@alt').extract()[0]
            # item['link'] = "https://kith.com" + product.xpath('div/div/a[1]/@href').extract()[0]
            # item['image'] = "https:" + product.xpath('div/div/a[1]/img/@src').extract()[0]
            # item['size'] = "https://kith.com/cart/add.js?id=" + product.xpath('div/div/a[2]/div/*/div[1]/@data-value').extract()[0] + "&quantity=1"
            # yield item
            yield {
                # 'name': product.xpath('div[@class="product-card__information"]/div[@class="product-card__title"]').extract()[0],
                # 'price': product.xpath('div[@class="product-card__information"]/div[@class="product-card__price"]').extract()[0],
                'name': product.css('div.product-card__information h1.product-card__title::text').get(),
                'price':product.css('div.product-card__information span.product-card__price::text').get(),
                'link': product.css('div.product-card__information span.product-card__price::text').get()
            }

        # yield Request(KithURL, callback=self.parse, dont_filter=True, priority=0)

# crawler_settings = Settings()
# crawler_settings.setmodule(settings)
# process = CrawlerProcess(settings=crawler_settings)
# process.crawl(KithSpider)
# process.start()
