"""Settings for drive2day"""

BOT_NAME = 'drive2day'

SPIDER_MODULES = ['tsei_scraper_drive2day.spiders']

SPIDER_MIDDLEWARES = {
    'scrapy.extensions.closespider.CloseSpider': 50,
    'scrapy_magicfields.MagicFieldsMiddleware': 100,
    'scrapy_deltafetch.DeltaFetch': 200,
}

ITEM_PIPELINES = {
    'tsei_lib.pipelines.VerifyPipeline': 500,
    'tsei_lib.pipelines.MongoDBPipeline': 1000,
}

DELTAFETCH_ENABLED = True
CLOSESPIDER_ERRORCOUNT = 1

USER_AGENT = 'ZetaDeltaBot (info@zd.ee)'
DOWNLOAD_DELAY = 1.0
AUTOTHROTTLE_ENABLED = True

# Magic fields
MAGIC_FIELDS = {
    "_time": "$time",
}

# MongoDB Pipeline
MONGO_URI = "mongodb://localhost:27017/"
MONGO_DB = "tsei"
MONGO_COLLECTION = "drive2day"

# HTTP Cache
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
