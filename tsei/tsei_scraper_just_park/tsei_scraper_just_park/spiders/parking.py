"""
################################################################################
justPark: parking map scraper.
################################################################################
## notes to myself:

Takes an argument through crawl -a days=int

=====

Note:
=====


"""
import datetime
import json
from tsei_scraper_just_park.items import JustParkListingItem
import scrapy
from pymongo import MongoClient
from scrapy.http import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Compose
from scrapy.selector import Selector
from scrapy.utils.python import unique
from scrapy.utils.response import get_base_url


class ParkingSpider(scrapy.Spider):
    """Map scraper for justPark"""
    name = "parking"
    allowed_domains = ["justpark.com"]

    def __init__(self, days='', *args, **kwargs):
        super(ParkingSpider, self).__init__(*args, **kwargs)
        self.tsei_collection = MongoClient().tsei
        self.days = int(days)

    def start_requests(self):
        s_date = datetime.date.today()
        start_date = datetime.date.today().strftime("%e%%20%b%%20%Y")
        e_date = s_date + datetime.timedelta(self.days)
        end_date = e_date.strftime("%e%%20%b%%20%Y")
        return [Request("http://www.justpark.com/search/bounding-box/?end_date={}&end_time=18%3A00%3A00&nw_lat=90.079355565750576&nw_lng=-180.20887790869142&se_lat=-90.07071130221634&se_lng=180.8676150913086076&start_date={}&start_time=08%3A00%3A00".format(end_date, start_date))]



    def parse(self, response):
        listing = json.loads(response.body.decode("utf-8"))
        item = listing
        print("xxxxxx", listing)
        item = JustParkListingItem()
        for key, value in listing.items():
            if key in JustParkListingItem.fields:
                item[key] = value
        yield item
