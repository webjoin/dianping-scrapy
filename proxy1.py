#coding=utf-8
import requests

#请求地址
targetUrl = "http://baidu.com"
targetUrl = 's9.proxy.mayidaili.com'
targetUrl = 'http://members.3322.org/dyndns/getip'

#代理服务器
proxyHost = "114.103.20.126"
proxyPort = "4235"

proxyMeta = "http://%(host)s:%(port)s" % {

    "host" : proxyHost,
    "port" : proxyPort,
}

#pip install -U requests[socks]  socks5代理
# proxyMeta = "socks5://%(host)s:%(port)s" % {

#     "host" : proxyHost,

#     "port" : proxyPort,

# }

proxies = {
    "http":proxyMeta,
}

resp = requests.get(targetUrl, proxies=proxies)
print(resp.status_code)
print(resp.text)
