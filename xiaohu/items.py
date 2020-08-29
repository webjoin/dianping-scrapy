# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XiaohuBasicInfoItem(scrapy.Item):
    # define the fields for your item here like:

    _id = scrapy.Field()  # _id 即使是mongodb默认添加，也需要在这里定义

    register_no = scrapy.Field()
    test_status = scrapy.Field()
    register_name = scrapy.Field()
    register_date = scrapy.Field()
    register_company = scrapy.Field()

    # pass





class xiaohuShopStatusItem(scrapy.Item):
    # define the fields for your item here like:

    _id = scrapy.Field()  # _id 即使是mongodb默认添加，也需要在这里定义

    shop_id = scrapy.Field()
    shop_name = scrapy.Field()
    shop_status = scrapy.Field()
    # pass

