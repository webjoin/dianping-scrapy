# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urlencode
import datetime
from ..items import XiaohuBasicInfoItem
from ..dictionary1 import useragent
import random


class HucdcSpider(scrapy.Spider):
    name = 'chinadrugtrials'
    allowed_domains = ['xiaohu.com']
    # start_urls = ['http://www.xiaohu.com/shanghai/ch30/g141']
    # start_urls = ['http://www.xiaohu.com/']

    manualRetry = 8
    custom_settings = {
        'DOWNLOAD_DELAY': 1,  # 下载延时 250 ms of delay
        'LOG_LEVEL': 'INFO',  # 定义log等级
        'LOG_FILE': 'abc_log_%s.txt' % datetime.time(),
        'COOKIES_ENABLED': False,  # enabled by default
        'DEFAULT_REQUEST_HEADERS': {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,ja;q=0.8,zh;q=0.6,en-US;q=0.4,en;q=0.2',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Host': 'www.xiaohu.com',
            'Pragma': 'no-cache',
            'Cookie': '_lxsdk_cuid=16168f28064c8-03adfcfa14529e8-495960-13c680-16168f28064c8; _lxsdk=16168f28064c8-03adfcfa14529e8-495960-13c680-16168f28064c8; cityid=1; _hc.v=9e5f15b5-7d19-6bdc-f960-bd2da02ef00b.1521881183; switchcityflashtoast=1; s_ViewType=10; cy=1; cye=shanghai; _lxsdk_s=1637476af70-7ac-fe1-27e%7C%7C27',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:59.0) Gecko/20100101 Firefox/59.0'
        },
        'DOWNLOADER_MIDDLEWARES': {
            #     # 'fengniao.middlewares.ProxiesMiddleware': 400,
            'xiaohu.middlewares.HeadersMiddleware': 543,
            # 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
        },
        'scrapy.middleware': {

        }
    }

    def get_origin_urls(self):
        urls = [
            'http://www.chinadrugtrials.org.cn/clinicaltrials.searchlistdetail.dhtml',
        ]

        return urls

    def start_requests(self):
        self.logger.info("-------->>start_requests")

        urls = self.get_origin_urls()

        for url_pattern in urls:
            page_num = 0
            # req_url_pattern = "http://www.xiaohu.com/shanghai/ch30/g141p{}"
            print('url_pattern,page_num', url_pattern, '-------------', page_num)
            url = url_pattern
            post_data = dict(
                currentpage=1,
                sort="desc",
                sort2="desc",
                rule="CTR"
            )
            yield scrapy.Request(url=url,
                                 # headers=headers,
                                 method='POST',
                                 body=urlencode(post_data),
                                 meta={'dont_redirect': True, 'pageNum': page_num + 1, 'req_url_pattern': url_pattern},
                                 callback=self.parseArticle,  # 指定处理Response的函数
                                 errback=self.error
                                 )

    def parseArticle(self, response):
        print(" response.text parseArticle %s", response.text)
        basicInfoTable = response.xpath('//*[@id="collapseOne"]/div/table')
        self.logger.info("-------->>%s", basicInfoTable)
        isGetNextPage = False

        print('isGetNextPage', isGetNextPage)
        dpItem = XiaohuBasicInfoItem()

        dpItem['register_no'] = basicInfoTable.xpath('./tbody/tr[1]/td[1]/text()').extract()  # 登记号
        dpItem['test_status'] = basicInfoTable.xpath('./tbody/tr[1]/td[2]/text()').extract()  # 试验状态
        dpItem['register_name'] = basicInfoTable.xpath('./tbody/tr[2]/td[1]/text()').extract()  # 申请人联系人
        dpItem['register_date'] = basicInfoTable.xpath('./tbody/tr[2]/td[2]/text()').extract()  # 首次公示信息日期
        dpItem['register_company'] = basicInfoTable.xpath('./tbody/tr[3]/td[1]/text()').extract()  # 申请人名称

        yield dpItem

        self.logger.info("-------->>end")

        # if isGetNextPage is True:
        #     pageNum = meta['pageNum']
        #     req_url = meta['req_url_pattern'].format(pageNum)
        #     meta['pageNum'] = pageNum + 1
        #     self.logger.info("正在请求---------------------->>>{}".format(req_url))
        #     yield scrapy.Request(url=req_url,
        #                          # headers=headers,
        #                          meta=meta,
        #                          callback=self.parseArticle,  # 指定处理Response的函数
        #                          errback=self.error
        #                          )

    def error(self, response):
        self.logger.info("-------->>error")
        pass
