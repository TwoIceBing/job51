# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class ZhaopinPipeline(object):
    def open_spider(self, spider):
        self.db = pymysql.connect(host='localhost',user='root',password='root',database='zhaopin',port=3306,charset='utf8')
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        sql = 'insert into job' \
              '(jobname,company,work_place,salary,joblink,pub_time,work_exp,edu,call_num,company_pro,company_num,job_info,job_type) ' \
              'values("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")' % (
            item['jobname'],item['company'],item['work_place'],item['salary'],item['joblink'],item['pub_time'],item['work_exp'],item['edu'],item['call_num'],item['company_pro'],item['company_num'],item['job_info'],item['job_type']
        )
        self.cursor.execute(sql)
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.db.close()
