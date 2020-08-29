# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


class xiaohuPipeline(object):
    def __init__(self, mongoUrl, mongoDB):
        self.mongo_url = mongoUrl
        self.mongo_db = mongoDB

    # 从settings中拿到配置信息，这个方法是内置的
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongoUrl=crawler.settings.get("MONGO_URI"),
            mongoDB=crawler.settings.get("MONGO_DB")
        )

    # 在爬虫开始时会调用
    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_url)
        self.db = self.client[self.mongo_db]
        self.tab_chinadrugtrials = self.db['chinadrugtrials']
        self.tab_cfdi = self.db['cfdi']
        spider.logger.info('open the mongo db ........')
        pass

    def process_item(self, item, spider):
        spider.logger.info("chinadrugtrials: item = %s}", item)
        try:
            insertRes = self.tab_chinadrugtrials.insert_one(item)
            spider.logger.info("chinadrugtrials: insertRes = %s", insertRes.inserted_id)
        except Exception as e:
            # 如果在try部份引发异常，则执行这段代码
            spider.logger.info("chinadrugtrials: insertRes(hucdc) Exception = %s", e)
        else:
            # 如果没有异常发生，则执行这段代码
            # raise DropItem("hucdc record inserted!")
            spider.logger.info("finely chinadrugtrials : insertRes = %s", insertRes.inserted_id)

            pass
            # return item
            # # save to csv file
            # # myClassJson = json.dumps(item)
            # json_str = self.xiaohuItem_2_json(daipingItem=item)
            # filename = 'data/hucdc.csv'
            # # 'a'表示append,即在原来文件内容后继续写数据（不清楚原有数据）
            # with open(filename, 'a') as f:
            #     f.write(json_str)
            #     f.write("\n")

    def xiaohuItem_2_json(self, daipingItem):
        dict1 = daipingItem.__dict__['_values']
        print('---------------<<<', dict1)
        values = []
        for key in dict1:
            values.append(dict1[key])

        return ",".join(values)

    # # 在爬虫结束时会调用
    def close_spider(self, spider):
        spider.logger.info("close_spider..............")
        self.client.close()
        # pass
