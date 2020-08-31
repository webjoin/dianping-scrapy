# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

import base64

from .items import ip_pool
from .dictionary1 import useragent
import random
import base64
import time
import hashlib


class HeadersMiddleware:

    def base_code(self, username1, password):
        str = '%s:%s' % (username1, password)
        encodestr = base64.b64encode(str.encode('utf-8'))
        return '%s' % encodestr.decode()

    def generate_sign(self):
        appkey = "154900555"
        secret = "76f409cee11dbf48a8168c462dcbc77f"
        mayi_url = "s9.proxy.mayidaili.com"
        mayi_port = "8123"
        mayi_proxy = 'http://{}:{}'.format(mayi_url, mayi_port)

        paramMap = {
            "app_key": appkey,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }

        keys = sorted(paramMap)
        codes = "%s%s%s" % (secret, str().join('%s%s' % (key, paramMap[key]) for key in keys), secret)

        sign = hashlib.md5(codes.encode('utf-8')).hexdigest().upper()

        paramMap["sign"] = sign

        keys = paramMap.keys()
        authHeader = "MYH-AUTH-MD5 " + str('&').join('%s=%s' % (key, paramMap[key]) for key in keys)
        return authHeader, mayi_proxy

    def process_request(self, request, spider):
        authHeader, mayi_proxy = self.generate_sign()
        request.headers['User-Agent'] = random.choice(useragent)
        request.headers["Mayi-Authorization"] = authHeader

        # request.header
        # thisip = random.choice(ip_pool)
        # proxy = "http://" + thisip
        # proxy = "http://proxy.wandouip.com:8090"
        request.meta['proxy'] = mayi_proxy

        pass
