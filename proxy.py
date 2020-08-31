# Python 3.x

import hashlib
import time
import requests
from urllib.parse import urlencode

# 找群主购买 my_app_key, myappsecret, 以及蚂蚁代理服务器的 mayi_url 地址和 mayi_port 端口
my_app_key = "154900555"
app_secret = "76f409cee11dbf48a8168c462dcbc77f"
mayi_url = 's9.proxy.mayidaili.com'
mayi_port = '8123'

# 蚂蚁代理服务器地址
mayi_proxy = {'http': 'http://{}:{}'.format(mayi_url, mayi_port)}

# 准备去爬的 URL 链接
url = 'http://www.chinadrugtrials.org.cn/clinicaltrials.searchlistdetail.dhtml'
url = 'http://127.0.0.1:8080/hi'
url = 'http://www.baidu.com'
url = 'http://members.3322.org/dyndns/getip'
# url = 'http://tool.lu/ip'

# 计算签名
timesp = '{}'.format(time.strftime("%Y-%m-%d %H:%M:%S"))
codes = app_secret + 'app_key' + my_app_key + 'timestamp' + timesp + app_secret
sign = hashlib.md5(codes.encode('utf-8')).hexdigest().upper()

# 拼接一个用来获得蚂蚁代理服务器的「准入」的 header (Python 的 concatenate '+' 比 join 效率高)
authHeader = 'MYH-AUTH-MD5 sign=' + sign + '&app_key=' + my_app_key + '&timestamp=' + timesp

# 用 Python 的 Requests 模块。先订立 Session()，再更新 headers 和 proxies


for ii in range(1, 3):
    s = requests.Session()
    s.headers.update({'Proxy-Authorization': authHeader})
    # s.headers['Content-Type'] = 'application/x-www-form-urlencoded'
    s.proxies.update(mayi_proxy)
    post_data = dict(currentpage=1, sort="desc", sort2="desc", rule="CTR")
    pg = s.get(url, allow_redirects=True, timeout=(300, 270))  # tuple: 300 代表 connect timeout, 270 代表 read timeout
    # pg.encoding = 'GB18030'
    print(pg.text)
