# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


class DianpingPipeline(object):
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
        # self.db_table = self.db['shop-status-3']
        self.db_table = self.db['Massage-few-minhan']
        spider.logger.info('open the mongo db ........')
        pass

    def process_item(self, item, spider):
        # spider.logger.info(f"massage: item = {item}")
        try:
            insertRes = self.db_table.insert_one(item)
            # spider.logger.info(f"massage: insertRes = {insertRes.inserted_id}")
        except Exception as e:
            # 如果在try部份引发异常，则执行这段代码
            spider.logger.info(f"massage: insertRes(massage) Exception = {e}")
        else:
            # 如果没有异常发生，则执行这段代码
            # raise DropItem("massage record inserted!")
            pass
            # return item
            # # save to csv file
            # # myClassJson = json.dumps(item)
            # json_str = self.dianpingItem_2_json(daipingItem=item)
            # filename = 'data/massage.csv'
            # # 'a'表示append,即在原来文件内容后继续写数据（不清楚原有数据）
            # with open(filename, 'a') as f:
            #     f.write(json_str)
            #     f.write("\n")

    def dianpingItem_2_json(self, daipingItem):
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
