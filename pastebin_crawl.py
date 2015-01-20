import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.http import Request
import pymongo
from pymongo import MongoClient


from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log


from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy import  signals
from scrapy.utils.project import get_project_settings


#Define all setting for crawling

BOT_NAME = 'pastebin_crawl'

SPIDER_MODULES = ['pastebin_crawl.spiders']
NEWSPIDER_MODULE = 'pastebin_crawl.spiders'

DOWNLOAD_DELAY = 0.50
CONCURRENT_ITEMS = 200

#connect to mongoDB database
client = MongoClient('localhost', 27017)
db = client['test_database_py']
collection = db['test_collection']


class PastebinProjItem(scrapy.Item):
    # define the fields that need to be retrieved for crawling

    url = scrapy.Field()
    paste = scrapy.Field()
    time = scrapy.Field()
    uniq_visitors = scrapy.Field()

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
        items['uniq_visitors'] = response.xpath("//div[@class='paste_box_line2']//span[2]/text()").extrac$
        collection.insert(items)
        return items

print "-------------Check for data in mongoDB-------------------"

    
