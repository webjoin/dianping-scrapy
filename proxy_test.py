# coding:utf8
import requests
import time
import hashlib


def generate_sign():
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


def proxy_test():
    authHeader, mayi_proxy = generate_sign()
    headers = {
        "Mayi-Authorization": authHeader,
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1"
    }

    proxies = {
        "http": mayi_proxy,
        "https": mayi_proxy,
    }
    target_url = "http://www.qq.com"
    target_url = 'http://members.3322.org/dyndns/getip'
    response = requests.get(target_url, proxies=proxies, headers=headers, allow_redirects=False, verify=False)
    print(response.status_code)
    print(response.headers)
    print(response.content)


if __name__ == "__main__":
    ii = 3;
    if ii == 4:
        print('a')

    if ii == 3:
        print('b')

    # proxy_test()
