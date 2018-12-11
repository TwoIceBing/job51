# coding:utf-8
import pymysql


class Read(object):
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='root', database='zhaopin', port=3306, charset='utf8')
        self.cursor = self.db.cursor()

    def query_all(self):
        sql = "select * from job"
        self.cursor.executemany(sql)
        return self.cursor.fetchall()

    def que_one(self):
        sql = "select * from job"
        self.cursor.executemany(sql)
        return self.cursor.fetchone()

    def close(self):
        self.cursor.close()
        self.db.close()