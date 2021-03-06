# -*- coding: utf-8 -*-

# Scrapy settings for scrapy_demo project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'scrapy_demo'

SPIDER_MODULES = ['scrapy_demo.spiders']
NEWSPIDER_MODULE = 'scrapy_demo.spiders'
DOWNLOAD_DELAY = 0.50
CONCURRENT_ITEMS = 200

ITEM_PIPELINES = ['scrapy_demo.pipelines.ScrapyDemoPipeline', ]

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "test_database_py"
MONGODB_COLLECTION = "test_collection"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapy_demo (+http://www.yourdomain.com)'
