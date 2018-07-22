# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DianpingItem(scrapy.Item):
    # define the fields for your item here like:

    _id = scrapy.Field()  # _id 即使是mongodb默认添加，也需要在这里定义

    dpId = scrapy.Field()
    title = scrapy.Field()

    igroup = scrapy.Field()
    ibook = scrapy.Field()
    start = scrapy.Field()
    commentCount = scrapy.Field()
    avgPrice = scrapy.Field()
    type = scrapy.Field()
    biz_area = scrapy.Field()
    addr = scrapy.Field()
    branchShop = scrapy.Field()
    district = scrapy.Field()
    # pass





class DianpingShopStatusItem(scrapy.Item):
    # define the fields for your item here like:

    _id = scrapy.Field()  # _id 即使是mongodb默认添加，也需要在这里定义

    shop_id = scrapy.Field()
    shop_name = scrapy.Field()
    shop_status = scrapy.Field()
    # pass

