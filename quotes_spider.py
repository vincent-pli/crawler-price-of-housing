import scrapy
import re

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://xa.fang.anjuke.com/loupan/',
    ]

    def parse(self, response):
        print(len(response.css('div.key-list div.item-mod')))
        for quote in response.css('div.key-list div.item-mod'):
            yield {
                'name': quote.css('span.items-name::text').extract_first().encode("utf-8"),
                'price': quote.css('a.favor-pos span::text').extract_first(),
                'address': quote.css('a.address span::text').extract_first().encode("utf-8"),
                'category': quote.css('a.tags-wrap i.wuyetp::text').extract_first().encode("utf-8")
            }

        next_page = response.css('div.pagination a.next-page::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
