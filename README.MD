
scrapy 采集点评按摩商户信息

需要mongo环境 配置如下
dianping/settings.py/MONGO_URI
dianping/settings.py/MONGO_DB



0、命令scrapyd启动scrapy部署程序

1、部署到scrapyd 服务器上
    scrapyd-deploy dianping -p massage

2、启动 gerapy
      gerapy init
      cd gerapy
      gerapy migrate
      gerapy runserver

3、访问 gerapy
    http://127.0.0.1:8000/#/client

4、通过gerapy 来调度爬虫
   创建 client
   ip: 127.0.0.1
   port: 6800

5、找到massage 点击调度