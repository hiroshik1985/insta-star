# -*- coding: utf-8 -*-
import scrapy


class WikipediaSpider(scrapy.Spider):
    name = 'wikipedia'
    allowed_domains = ['ja.wikipedia.org']

    def start_requests(self):
        with open('name.csv', 'r') as f:
            for line in f:
                yield scrapy.Request('https://ja.wikipedia.org/wiki/%s' % line.rstrip('\n'), self.parse)

    def parse(self, response):
        pass
#        print(response)
