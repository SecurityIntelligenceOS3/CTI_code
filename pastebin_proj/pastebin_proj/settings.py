# -*- coding: utf-8 -*-

# Scrapy settings for pastebin_proj project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'pastebin_proj'

SPIDER_MODULES = ['pastebin_proj.spiders']
NEWSPIDER_MODULE = 'pastebin_proj.spiders'

DOWNLOAD_DELAY = 0.50
CONCURRENT_ITEMS = 200

ITEM_PIPELINES = ['pastebin_proj.pipelines.PastebinProjPipeline', ]

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "test_database_py"
MONGODB_COLLECTION = "test_collection"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'pastebin_proj (+http://www.yourdomain.com)'
