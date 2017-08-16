# -*- coding: utf-8 -*-
import scrapy


class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'toscrape-xpath'
    start_urls = [
        'https://twitter.com/search?l=id&q=%3A)&src=typd',
    ]

    def parse(self, response):
        for quote in response.xpath('//div[@class="js-tweet-text-container"]'):
            yield {
                'text' : quote.xpath('.//p[@class="TweetTextSize  js-tweet-text tweet-text"]/text()').extract_first()
                
            }

        next_page_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))

