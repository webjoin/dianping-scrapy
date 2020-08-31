# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urlencode
import datetime
from ..items import ChinadrugtrialsInfoItem
from ..items import BaseItem
from ..items import ResearcherItem
from ..items import InstsItem
from ..items import BackItem
from ..items import StatusItem
from ..dictionary1 import useragent
import random


class HucdcSpider(scrapy.Spider):
    name = 'chinadrugtrials'
    allowed_domains = ['xiaohu.com']
    # start_urls = ['http://www.xiaohu.com/shanghai/ch30/g141']
    # start_urls = ['http://www.xiaohu.com/']

    manualRetry = 2
    custom_settings = {
        'DOWNLOAD_DELAY': 0.20,  # 下载延时 250 ms of delay
        'LOG_LEVEL': 'INFO',  # 定义log等级
        # 'LOG_FILE': 'abc_log_%s.txt' % datetime.time(),
        # 'COOKIES_ENABLED': False,  # enabled by default
        'DEFAULT_REQUEST_HEADERS': {
            'Content-Type': 'application/x-www-form-urlencoded',
            # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            # 'Accept-Encoding': 'gzip, deflate',
            # 'Accept-Language': 'zh-CN,ja;q=0.8,zh;q=0.6,en-US;q=0.4,en;q=0.2',
            # 'Cache-Control': 'no-cache',
            # 'Connection': 'keep-alive',
            # 'Host': 'www.xiaohu.com',
            # 'Pragma': 'no-cache',
            # 'Cookie': '_lxsdk_cuid=16168f28064c8-03adfcfa14529e8-495960-13c680-16168f28064c8; _lxsdk=16168f28064c8-03adfcfa14529e8-495960-13c680-16168f28064c8; cityid=1; _hc.v=9e5f15b5-7d19-6bdc-f960-bd2da02ef00b.1521881183; switchcityflashtoast=1; s_ViewType=10; cy=1; cye=shanghai; _lxsdk_s=1637476af70-7ac-fe1-27e%7C%7C27',
            # 'Upgrade-Insecure-Requests': '1',
            # 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:59.0) Gecko/20100101 Firefox/59.0'
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Cookie': 'FSSBBIl1UgzbN7N80S=S3xyqTBd2I86j5aJD4ZfKPfGSaE4xsbZ6GER1cbvTV.JZ9TV9mk6frCh33kbjI16; token=M9__sw6CszVNI2WX69i0493-LWX3_Hm_PxXDMrOludY4ua0dCTixzSDOnvR; FSSBBIl1UgzbN7N80T=3iMuLGrQlIBJlUy03zx8buvHCY6PXv_aOm0j5QkZoECkm_7K7JKPAOorz93WJwEUvVTJjXOWwUIoCBRggizZybgOgSipVLfDzjeCyx8u3Ej84mmxmzhX7DGLiz4LCwB04BF51Sg.ftIwjDkFoZGu7xVIJpahybuoLkeAPEw38JxYPN_iMKr6LXGZg4LuqxMyno0cfLNUf8XF26i8O5r5w.BD8hRPfgD0LlJr55ZbM.gUC9NUcmYAhrwKyVL9XwBpyw.5mUIK0nD4Hokvpgh9B03HOEsbinIy.kN6dWh0QCifgeEQZ.JM2fZZW5JZKOMeNyF3Y__Las9Yp_BBOkahilcgWlyY28rKLWPTTWcLwswlufG',
            # 'Host': 'www.chinadrugtrials.org.cn',
            'Pragma': 'no-cache',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
        },
        'DOWNLOADER_MIDDLEWARES': {
            #     # 'fengniao.middlewares.ProxiesMiddleware': 400,
            'xiaohu.middlewares.HeadersMiddleware': 543,
            # 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
        },
        'scrapy.middleware': {

        }
    }

    def start_requests(self):
        self.logger.info("----HeadersMiddleware---->>start_requests")
        curr_page = 2462
        curr_page = 9301
        req_url = ''.join(
            ['h', 't', 't', 'p', ':', '/', '/', 'w', 'w', 'w', '.', 'c', 'h', 'i', 'n', 'a', 'd', 'r', 'u', 'g', 't',
             'r', 'i', 'a', 'l', 's', '.', 'o', 'r', 'g', '.', 'c', 'n', '/', 'c', 'l', 'i', 'n', 'i', 'c', 'a', 'l',
             't', 'r', 'i', 'a', 'l', 's', '.', 's', 'e', 'a', 'r', 'c', 'h', 'l', 'i', 's', 't', 'd', 'e', 't', 'a',
             'i', 'l', '.', 'd', 'h', 't', 'm', 'l'])
        # req_url = 'http://127.0.0.1:8080/hi'
        # req_url = 'http://members.3322.org/dyndns/getip'
        post_data = dict(currentpage=curr_page, sort="desc", sort2="desc", rule="CTR")
        yield scrapy.Request(url=req_url + '?pa=' + str(curr_page),
                             method='POST',
                             body=urlencode(post_data),
                             meta={'dont_redirect': True, 'curr_page': curr_page, 'req_url': req_url},
                             callback=self.parseArticle,  # 指定处理Response的函数
                             errback=self.error,
                             dont_filter=True
                             )

    def parseArticle(self, response):
        print(" response.text parseArticle %s", response.text)
        meta_param = response.meta
        basic_info_table = response.xpath('//*[@id="collapseOne"]/div/table')
        curr_page = int(response.xpath('//*[@id="toolbar_top"]/div/span[1]/text()').extract_first())
        total_page = 10000 #int(response.xpath('//*[@id="toolbar_top"]/div/span[2]/text()').extract_first())
        # self.logger.info("111-------->>%s", basic_info_table)

        info_item = ChinadrugtrialsInfoItem()
        info_item['curr_page'] = curr_page
        info_item['base_inf'] = getBaseItem(basic_info_table, curr_page)
        info_item['researcher_inf'] = getResearcherItem(response, curr_page)
        info_item['insts_inf'] = getInstsItem(response, curr_page)
        info_item['back_inf'] = getBackItem(response, curr_page)
        info_item['status_inf'] = getStatusItem(response, curr_page)
        yield info_item

        self.logger.info("-------->>continue ？")
        if total_page > curr_page:
            curr_page = meta_param['curr_page']
            meta_param['curr_page'] = curr_page + 1
            req_url = meta_param['req_url'] + '?page=' + str(meta_param['curr_page'])
            post_data = dict(currentpage=meta_param['curr_page'], sort="desc", sort2="desc", rule="CTR")
            self.logger.info("正在请求---------------------->>>{} 第{}页 总共{}".format(req_url, curr_page, total_page))
            yield scrapy.Request(url=req_url,
                                 method='POST',
                                 body=urlencode(post_data),
                                 meta=meta_param,
                                 callback=self.parseArticle,  # 指定处理Response的函数
                                 errback=self.error,
                                 dont_filter=True
                                 )
        self.logger.info("-------->>end")

    def error(self, failure):
        response = failure.value.response
        if 403 == response.status:
            meta_param = response.meta
            curr_page = meta_param['curr_page']
            req_url = meta_param['req_url'] + '?page=' + str(meta_param['curr_page'])
            post_data = dict(currentpage=meta_param['curr_page'], sort="desc", sort2="desc", rule="CTR")
            self.logger.info("正在请求---------------------->>>{} 第{}页 总共0页 失败重新请求".format(req_url, curr_page))
            yield scrapy.Request(url=req_url,
                                 method='POST',
                                 body=urlencode(post_data),
                                 meta=meta_param,
                                 callback=self.parseArticle,  # 指定处理Response的函数
                                 errback=self.error,
                                 dont_filter=True
                                 )
        if 504 == response.status:
            meta_param = response.meta
            curr_page = meta_param['curr_page']
            req_url = meta_param['req_url'] + '?page=' + str(meta_param['curr_page'])
            post_data = dict(currentpage=meta_param['curr_page'], sort="desc", sort2="desc", rule="CTR")
            self.logger.info("正在请求---------------------->>>{} 第{}页 总共0页 失败重新请求".format(req_url, curr_page))
            yield scrapy.Request(url=req_url,
                                 method='POST',
                                 body=urlencode(post_data),
                                 meta=meta_param,
                                 callback=self.parseArticle,  # 指定处理Response的函数
                                 errback=self.error,
                                 dont_filter=True
                                 )

        self.logger.error(repr(failure))
        self.logger.error(' 请求异常的响应状态：%s', response.status)
        pass


def getBaseItem(basic_info_table, curr_page):
    base_item = BaseItem()

    base_item['curr_page'] = curr_page
    base_item['登记号'] = basic_info_table.xpath('./tr[1]/td[1]/text()').extract_first('').strip()  # 登记号
    base_item['试验状态'] = basic_info_table.xpath('./tr[1]/td[2]/text()').extract_first('').strip()  # 试验状态
    base_item['申请人联系人'] = basic_info_table.xpath('./tr[2]/td[1]/text()').extract_first('').strip()  # 申请人联系人
    base_item['首次公示信息日期'] = basic_info_table.xpath('./tr[2]/td[2]/text()').extract_first('').strip()  # 首次公示信息日期
    base_item['申请人名称'] = basic_info_table.xpath('./tr[3]/td[1]/text()').extract_first('').strip()  # 申请人名称

    return base_item


def getResearcherItem(response, curr_page):
    researcherItem = ResearcherItem()
    table_infs = response.xpath('//*[@id="collapseTwo"]/div/table[7]')

    researcherItem['curr_page'] = curr_page
    researcherItem['姓名'] = table_infs.xpath('./tr[1]/td[1]/text()').extract_first('').strip()
    researcherItem['学位'] = table_infs.xpath('./tr[1]/td[2]/text()').extract_first('').strip()
    researcherItem['职称'] = table_infs.xpath('./tr[1]/td[3]/text()').extract_first('').strip()

    researcherItem['电话'] = table_infs.xpath('./tr[2]/td[1]/text()').extract_first('').strip()
    researcherItem['Email'] = table_infs.xpath('./tr[2]/td[2]/text()').extract_first('').strip()
    researcherItem['邮政地址'] = table_infs.xpath('./tr[2]/td[3]/text()').extract_first('').strip()

    researcherItem['邮编'] = table_infs.xpath('./tr[3]/td[1]/text()').extract_first('').strip()
    researcherItem['单位名称'] = table_infs.xpath('./tr[3]/td[2]/text()').extract_first('').strip()

    return researcherItem


def getInstsItem(response, curr_page):
    instsItems = []
    tr_infs = response.xpath('//*[@id="collapseTwo"]/div/table[8]/tr')
    # [2]/td[2]
    index = 0
    for tr_inf in tr_infs:
        if index > 0:
            instsItem = InstsItem()
            instsItem['curr_page'] = curr_page
            instsItem['机构名称'] = tr_inf.xpath('./td[2]/text()').extract_first('').strip()
            instsItem['主要研究者'] = tr_inf.xpath('./td[3]/text()').extract_first('').strip()
            instsItem['国家'] = tr_inf.xpath('./td[4]/text()').extract_first('').strip()
            instsItem['省_州'] = tr_inf.xpath('./td[5]/text()').extract_first('').strip()
            instsItem['城市'] = tr_inf.xpath('./td[6]/text()').extract_first('').strip()
            instsItems.append(instsItem)
        index = index + 1
    return instsItems


def getBackItem(response, curr_page):
    backItem = BackItem()

    tr_infs = response.xpath('//*[@id="collapseTwo"]/div/table[1]')
    backItem['curr_page'] = curr_page
    backItem['登记号'] = tr_infs.xpath('./tr[1]/td[1]/text()').extract_first('').strip()
    backItem['相关登记号'] = tr_infs.xpath('./tr[2]/td[1]/text()').extract_first('').strip()
    backItem['药物名称'] = tr_infs.xpath('./tr[3]/td[1]/text()').extract_first('').strip()
    backItem['药物类型'] = tr_infs.xpath('./tr[4]/td[1]/text()').extract_first('').strip()
    backItem['临床申请受理号'] = tr_infs.xpath('./tr[5]/td[1]/text()').extract_first('').strip()
    backItem['适应症'] = tr_infs.xpath('./tr[6]/td[1]/text()').extract_first('').strip()
    backItem['试验专业题目'] = tr_infs.xpath('./tr[7]/td[1]/text()').extract_first('').strip()
    backItem['试验通俗题目'] = tr_infs.xpath('./tr[8]/td[1]/text()').extract_first('').strip()
    backItem['试验方案编号'] = tr_infs.xpath('./tr[9]/td[1]/text()').extract_first('').strip()
    backItem['方案最新版本号'] = tr_infs.xpath('./tr[9]/td[2]/text()').extract_first('').strip()
    backItem['版本日期'] = tr_infs.xpath('./tr[10]/td[1]/text()').extract_first('').strip()
    backItem['方案是否为联合用药'] = tr_infs.xpath('./tr[10]/td[2]/text()').extract_first('').strip()
    return backItem


def getStatusItem(response, curr_page):
    statusItem = StatusItem()

    # //div[@class="sDPTit2"][contains(string(),'试验状态')]/following-sibling::text()
    statusItem['试验状态'] = response.xpath(
        '//div[@class="sDPTit2"][contains(string(),"试验状态")]/following-sibling::text()').extract_first('').strip()

    #
    tr_infs = response.xpath('//*[@id="collapseTwo"]/div/table[10]')
    statusItem['curr_page'] = curr_page
    statusItem['目标入组人数'] = tr_infs.xpath('./tr[1]/td[1]/text()').extract_first('').strip()
    statusItem['已入组人数'] = tr_infs.xpath('./tr[2]/td[1]/text()').extract_first('').strip()
    statusItem['实际入组总人数'] = tr_infs.xpath('./tr[3]/td[1]/text()').extract_first('').strip()

    return statusItem
