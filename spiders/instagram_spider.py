# -*- coding: utf-8 -*-
import scrapy


class InstagramSpiderSpider(scrapy.Spider):
    name = 'instagram_spider'
    allowed_domains = ['www.talentinsta.com']
    start_urls = [
        'http://www.talentinsta.com/tllink/ct_0'
        'http://www.talentinsta.com/tllink/ct_1',
        'http://www.talentinsta.com/tllink/ct_2',
        'http://www.talentinsta.com/tllink/ct_3',
        'http://www.talentinsta.com/tllink/ct_4',
        'http://www.talentinsta.com/tllink/ct_5',
        'http://www.talentinsta.com/tllink/ct_6',
        'http://www.talentinsta.com/tllink/ct_7',
        'http://www.talentinsta.com/tllink/ct_9',
        'http://www.talentinsta.com/tllink/ct_15',
        'http://www.talentinsta.com/tllink/ct_8',
        'http://www.talentinsta.com/tllink/ct_16',
        'http://www.talentinsta.com/tllink/ct_14',
        'http://www.talentinsta.com/tllink/ct_19',
        'http://www.talentinsta.com/tllink/ct_13',
        'http://www.talentinsta.com/tllink/ct_11',
        'http://www.talentinsta.com/tllink/ct_10'
    ]

    def parse(self, response):
        for link in response.xpath('//span/p/a/@href').extract():
            yield response.follow(link, self.parse_detail)
        next_page = response.xpath("/html/body/div[1]/table[5]//a[contains(text(), '次')]/@href").extract_first()
        if next_page:
            yield response.follow(next_page, self.parse)

    def parse_detail(self, response):
        name = response.xpath('//td/h1/text()').extract_first()
        account = response.xpath('//td/h2/a/@href').extract_first()
        yield {'name':name, 'account':account}