"""Items for saving justPark listings"""
import scrapy

from tsei_lib.items import ListingItem, SupplierItem


class JustParkListingItem(ListingItem):
    """justPark listing item"""

    class Meta(ListingItem.Meta):
        collection = "justPark_listing"
        key = "status"

    status = scrapy.Field()
    title = scrapy.Field()
    category_title = scrapy.Field()
    slug = scrapy.Field()
    truncated_price = scrapy.Field()
    id_id = scrapy.Field()
    truncated_price = scrapy.Field()
    lat = scrapy.Field()
    lng = scrapy.Field()
    reviews = scrapy.Field()
    no_of_spaces = scrapy.Field()
    start_date_time = scrapy.Field()
    end_date_time = scrapy.Field()
    url = scrapy.Field()
    price = scrapy.Field()
     


class JustParkSupplierItem(SupplierItem):
    """justPark listing item"""

