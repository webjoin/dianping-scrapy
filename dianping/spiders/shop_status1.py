# -*- coding: utf-8 -*-
import scrapy

from ..items import DianpingShopStatusItem
from ..dictionary1 import useragent
from ..dictionary1 import headers1
import codecs
import random
import time
import json


class ShopStatus1Spider(scrapy.Spider):
    name = 'shop-status1'
    allowed_domains = ['dingping.com']
    start_urls = ['http://dingping.com/']

    manualRetry = 0
    custom_settings = {
        'DOWNLOAD_DELAY': 0.3,  # 下载延时
        'LOG_LEVEL': 'INFO',  # 定义log等级
        'COOKIES_ENABLED': False,  # enabled by default
        # 'RANDOMIZE_DOWNLOAD_DELAY': False,
        # 'DOWNLOAD_DELAY': 60 / 40.0,
        # 'CONCURRENT_REQUESTS_PER_IP': 40,

        'DEFAULT_REQUEST_HEADERS': headers1,
        'DOWNLOADER_MIDDLEWARES': {
            #     # 'fengniao.middlewares.ProxiesMiddleware': 400,
            # 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
            # 'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 543,
            # 'dianping.middlewares.HeadersMiddleware': 125
            'dianping.middlewares.HeadersMiddleware': 543
        },
        'scrapy.middleware': {

        }
    }

    def read_shop_names_with_file(self):
        # filename = 'logger_data.txt'
        filename = '/Users/Elijah/Desktop/2018/July/点评ID'
        # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
        with codecs.open(filename, 'r', 'utf-8') as f:
            return f.readlines()

    def getTimestamp(self):
        t = time.time()
        nowTime = lambda: int(round(t * 1000))
        return nowTime()

    def start_requests(self):
        self.logger.info("-------->>start_requests")

        req_url_pattern = "http://www.dianping.com/poi/assistance/getshoppower.action?shopId={}&model=0&_nr_force={}"

        shopIds = self.read_shop_names_with_file()
        ii = 0
        for shopId in shopIds:
            ii = ii + 1
            shopId = shopId.strip()
            url = req_url_pattern.format(shopId, self.getTimestamp())
            self.logger.info(str(ii) + "-------->>--->>" + url)

            headers1['User-Agent'] = random.choice(useragent)
            print(headers1['User-Agent'])
            headers2 = headers1

            yield scrapy.Request(url=url,
                                 # headers=headers,
                                 meta={
                                     # 'dont_redirect': True,
                                     'shop_id': shopId, 'ii': ii},
                                 callback=self.paseArticle1,  # 指定处理Response的函数
                                 errback=self.error,
                                 headers=headers2

                                 )

            # break

            # yield scrapy.Request(url='http://ip.chinaz.com/getip.aspx',
            #                      # 指定处理Response的函数
            #                      callback=self.paseArticle2
            #                      # errback=self.error
            #                      )

    def paseArticle2(sefl, response):
        print(response.text)

    def paseArticle1(sefl, response):
        meta = response.meta
        ii = meta['ii']
        shop_id = meta['shop_id']

        print('正在采集第' + str(ii) + "个-----店ID：" + shop_id + "------------parseArticle")
        # status = response.xpath('//*[@id="basic-info"]/p').extract()

        jsonObj = json.loads(response.text)
        sefl.logger.info(jsonObj)
        code = jsonObj['code']
        if 200 == code:
            msg = jsonObj['msg']
            if not msg is None:
                powerString = msg['powerString']

        dpItem1 = DianpingShopStatusItem()
        dpItem1['shop_id'] = shop_id
        dpItem1['shop_status'] = powerString
        yield dpItem1

    def parseArticle(self, response):
        print(response)
        meta = response.meta
        ii = meta['ii']
        print(str(ii) + "-----------------parseArticle")
        # status = response.xpath('//*[@id="basic-info"]/p').extract()
        shop_id = meta['shop_id']
        status = response.xpath('//p[@class="shop-closed"]/text()').extract()
        shop_name = response.xpath('//*[@id="basic-info"]/h1/text()').extract()

        if len(shop_name) > 0:
            shop_name = shop_name[0].strip()
        else:
            shop_name = ''

        if len(status) > 0:
            for statu_text in status:
                emptyText = statu_text.strip()
                if emptyText != '':
                    status = emptyText;
        else:
            status = '正常'

        dpItem1 = DianpingShopStatusItem()
        dpItem1['shop_id'] = shop_id
        dpItem1['shop_name'] = shop_name
        dpItem1['shop_status'] = status
        yield dpItem1

    def error(self, response):
        # meta = response.meta
        # ii = meta['ii']
        # self.logger.info(str(ii) + "-----------------errs")
        print(response)
        self.logger.info("-----------------errs")
        pass
