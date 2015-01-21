from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from pastebin_proj.items import PastebinProjItem
from scrapy.http import Request
import pymongo

from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log



class PastebinSpider(CrawlSpider):

    name = 'pastebin'
    allowed_domains = ['pastebin.com']
    start_urls = ['http://www.pastebin.com/archive']
    rules = [Rule(LinkExtractor(allow=['/[a-zA-Z]*\d*']), 'parse_items')]

    def parse_items(self, response):
        items = PastebinProjItem()
        items['url'] = response.url
        items['paste'] = response.xpath("//textarea[@id='paste_code']/text()").extract()
	#span element= title="Thursday 15th of January 2015 07:43:17 AM CDT""
	items['time'] = response.xpath("//div[@class='paste_box_line2']//span[1]/@title").extract()
	items['uniq_visitors'] = response.xpath("//div[@class='paste_box_line2']//span[2]/text()").extract()
        return items


