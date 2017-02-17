"""Items for saving drive2day listings"""
import scrapy

from tsei_lib import ListingItem, SupplierItem


class Drive2DayListingItem(ListingItem):
    """drive2day listing item"""
    some_data = scrapy.Field()

class Drive2DaySupplierItem(SupplierItem):
    """drive2day listing item"""
    some_data = scrapy.Field()
