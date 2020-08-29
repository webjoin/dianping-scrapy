# -*- coding: utf-8 -*-
import scrapy

from ..items import DianpingItem
from ..dictionary1 import useragent
import random


class MassageSpider(scrapy.Spider):
    name = 'massage'
    allowed_domains = ['dianping.com']
    # start_urls = ['http://www.dianping.com/shanghai/ch30/g141']
    # start_urls = ['http://www.dianping.com/']

    manualRetry = 8
    custom_settings = {
        'DOWNLOAD_DELAY': 1,  # 下载延时
        'LOG_LEVEL': 'INFO',  # 定义log等级
        'COOKIES_ENABLED': False,  # enabled by default
        'DEFAULT_REQUEST_HEADERS': {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,ja;q=0.8,zh;q=0.6,en-US;q=0.4,en;q=0.2',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Host': 'www.dianping.com',
            'Pragma': 'no-cache',
            'Cookie': '_lxsdk_cuid=16168f28064c8-03adfcfa14529e8-495960-13c680-16168f28064c8; _lxsdk=16168f28064c8-03adfcfa14529e8-495960-13c680-16168f28064c8; cityid=1; _hc.v=9e5f15b5-7d19-6bdc-f960-bd2da02ef00b.1521881183; switchcityflashtoast=1; s_ViewType=10; cy=1; cye=shanghai; _lxsdk_s=1637476af70-7ac-fe1-27e%7C%7C27',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:59.0) Gecko/20100101 Firefox/59.0'
        },
        'DOWNLOADER_MIDDLEWARES': {
            #     # 'fengniao.middlewares.ProxiesMiddleware': 400,
            'dianping.middlewares.HeadersMiddleware': 543,
            # 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
        },
        'scrapy.middleware': {

        }
    }

    def get_origin_urls(self):
        urls = [
            'http://www.dianping.com/shanghai/ch30/r2869p{}',
        ]

        return urls

    def start_requests(self):
        self.logger.info("-------->>start_requests")

        urls = self.get_origin_urls()

        for url_pattern in urls:
            page_num = 0
            # req_url_pattern = "http://www.dianping.com/shanghai/ch30/g141p{}"
            print('url_pattern,page_num', url_pattern,'-------------', page_num)
            url = url_pattern.format(page_num)
            yield scrapy.Request(url=url,
                                 # headers=headers,
                                 meta={'dont_redirect': True, 'pageNum': page_num + 1, 'req_url_pattern': url_pattern},
                                 callback=self.parseArticle,  # 指定处理Response的函数
                                 errback=self.error
                                 )

    def parseArticle(self, response):
        print("-----------------parseArticle")
        divs = response.xpath('//*[@id="shop-all-list"]/ul/li')
        self.logger.info("-------->>start")
        articleLst = response.xpath('/html/body/div[2]/div[3]/div[1]/div[2]/a[@class="next"]/text()').extract()
        print(articleLst)
        district = response.xpath('/html/body/div[2]/div[1]/span[5]/a/span/text()').extract()[0]
        meta = response.meta
        isGetNextPage = False
        # if len(articleLst) > 0:
        #     isGetNextPage = True

        print('isGetNextPage', isGetNextPage)

        for div in divs:
            title = div.xpath('./div[2]/div[1]/a[1]/h4/text()').extract()

            # igroup1      = div.xpath('./div[2]/div[1]/div/a[@class="igroup1"]').extract()

            igroup = div.xpath('./div[2]/div[1]/div/a[@class="igroup"]/@class').extract()
            ibook = div.xpath('./div[2]/div[1]/div/a[@class="ibook "]/@class').extract()
            start = div.xpath("./div[2]/div[2]/span/@title").extract()
            commentCount = div.xpath("./div[2]/div[2]/a[1]/b/text()").extract()
            avgPrice = div.xpath("./div[2]/div[2]/a[2]/b/text()").extract()
            type = div.xpath("./div[2]/div[3]/a[1]/span/text()").extract()
            biz_area = div.xpath("./div[2]/div[3]/a[2]/span/text()").extract()
            addr = div.xpath("./div[2]/div[3]/span/text()").extract()
            dpUrlId = div.xpath("./div[2]/div[1]/a[@onclick]/@href").extract()
            branchShop = div.xpath('./div[2]/div[1]/a[@data-click-name="shop_branch_click"]/text()').extract()

            # print("------------->>",ibook.__len__())
            title_len = title.__len__()
            book_len = ibook.__len__()
            igroup_len = igroup.__len__()
            start_len = start.__len__()
            commentCount_len = commentCount.__len__()

            avgPrice_len = avgPrice.__len__()
            type_len = type.__len__()
            biz_area_len = biz_area.__len__()
            addr_len = addr.__len__()
            dpUrlId_len = dpUrlId.__len__()
            branchShop_len = branchShop.__len__()

            dpItem = DianpingItem()
            if title_len > 0:
                dpItem['title'] = title[0]
            if igroup_len > 0:
                dpItem['igroup'] = igroup[0]
            if book_len > 0:
                dpItem['ibook'] = ibook[0]

            if start_len > 0:
                dpItem['start'] = start[0]
            if commentCount_len > 0:
                dpItem['commentCount'] = commentCount[0]
            if avgPrice_len > 0:
                dpItem['avgPrice'] = avgPrice[0]
            if type_len > 0:
                dpItem['type'] = type[0]
            if biz_area_len > 0:
                dpItem['biz_area'] = biz_area[0]
            if addr_len > 0:
                dpItem['addr'] = addr[0]
            if dpUrlId_len > 0:
                dpItem['dpId'] = dpUrlId[0].replace('http://www.dianping.com/shop/', '')
            if branchShop_len > 0:
                dpItem['branchShop'] = branchShop[0].strip()

            dpItem['district'] = district.strip()

            yield dpItem
        self.logger.info("-------->>end")

        if isGetNextPage is True:
            pageNum = meta['pageNum']
            req_url = meta['req_url_pattern'].format(pageNum)
            meta['pageNum'] = pageNum + 1
            self.logger.info("正在请求---------------------->>>{}".format(req_url))
            yield scrapy.Request(url=req_url,
                                 # headers=headers,
                                 meta=meta,
                                 callback=self.parseArticle,  # 指定处理Response的函数
                                 errback=self.error
                                 )

    def error(self, response):
        self.logger.info("-------->>error")
        pass
