"""
################################################################################
drive2day: drivespider map scraper.
################################################################################

=====
Note:
=====

	* The above is probably not true.

"""

from geopy.distance import vincenty
import pandas
from tsei_scraper_drive2day.items import Drive2DayListingItem, Drive2DaySupplierItem
  
import scrapy
  
from scrapy.http import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Compose
from scrapy.selector import Selector
from scrapy.utils.python import unique
from scrapy.utils.response import get_base_url


class driveSpiderSpider(scrapy.Spider):
    """Map scraper for drive2day"""

    name = "drive_spider"
    allowed_domains = ["drive2day.com"]

    def start_requests(self):
		"""Create a list of request from each of the cities."""
        return [Request("http://project.com/search/")]

    def parse(self, response):
        """Parses the request"""
		il = ItemLoader(Drive2DayListingItem(), response)
		il.default_output_processor = Compose(lambda v: v[0], str.strip)

		il.add_value("listing_id", '//div[@class="id"]/text()')

		listing_item = il.load_item()
		yield listing_item

