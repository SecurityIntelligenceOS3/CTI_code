from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy_demo.items import ScrapyDemoItem
from scrapy.http import Request
import pymongo

from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log



class MininovaSpider(CrawlSpider):

    name = 'pastebin'
    allowed_domains = ['pastebin.com']
    start_urls = ['http://www.pastebin.com/archive']
    rules = [Rule(LinkExtractor(allow=['/[a-zA-Z]*\d*']), 'parse_items')]

    def parse_items(self, response):
        items = ScrapyDemoItem()
        items['url'] = response.url
        items['paste'] = response.xpath("//textarea[@id='paste_code']/text()").extract()
	items['time'] = response.xpath("//table[@class='maintable']//td[2]/text()").extract()
        return items
	return Request(response.url, callback=self.parse,dont_filter=True)


