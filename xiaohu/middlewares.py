# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

import base64


class HeadersMiddleware:
    def process_request(self, request, spider):
        print('i"m here -------- >>> Using HeadersMiddleware!')

        request.headers['Content-Type'] = 'application/x-www-form-urlencoded'
        # request.headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        # request.headers['Accept-Encoding'] = 'gzip, deflate',
        # request.headers['Accept-Language'] = 'zh-CN,ja;q=0.8,zh;q=0.6,en-US;q=0.4,en;q=0.2',
        # request.headers['Cache-Control'] = 'no-cache',
        # request.headers['Connection'] = 'keep-alive',
        # # request.headers['Cookie'] = '_lxsdk_cuid=16168f28064c8-03adfcfa14529e8-495960-13c680-16168f28064c8; _lxsdk=16168f28064c8-03adfcfa14529e8-495960-13c680-16168f28064c8; cityid=1; _hc.v=9e5f15b5-7d19-6bdc-f960-bd2da02ef00b.1521881183; switchcityflashtoast=1; s_ViewType=10; cy=1; cye=shanghai; _lxsdk_s=1637476af70-7ac-fe1-27e%7C%7C14',
        # request.headers['Cookie'] = 'lxsdk_cuid=16168f28064c8-03adfcfa14529e8-495960-13c680-16168f28064c8; _lxsdk=16168f28064c8-03adfcfa14529e8-495960-13c680-16168f28064c8; cityid=1; _hc.v=9e5f15b5-7d19-6bdc-f960-bd2da02ef00b.1521881183; switchcityflashtoast=1; s_ViewType=10; cy=1; cye=shanghai; _lxsdk_s=1637476af70-7ac-fe1-27e%7C%7C21',
        # request.headers['Host'] = 'www.xiaohu.com',
        # request.headers['Pragma'] = 'no-cache',
        # request.headers['Upgrade-Insecure-Requests'] = '1',

        # request.headers['User-Agent'] = random.choice(useragent)

        proxy = ""

        proxyUser = ""
        proxyPass = ""

        proxyAuth = "Basic " + base64.urlsafe_b64encode(bytes((proxyUser + ":" + proxyPass), "ascii")).decode("utf8")

        request.meta['proxy'] = proxy
        request.headers['Proxy-Authorization'] = proxyAuth

        pass
