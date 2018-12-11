# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhaopinItem(scrapy.Item):
    """
    jobname,company,work_place,salary,joblink,pub_time,work_exp,edu,call_num,company_pro,company_num,job_info,job_type
    """

    # 职位名
    jobname = scrapy.Field()

    # 公司名
    company = scrapy.Field()

    # 工作地点
    work_place = scrapy.Field()

    # 薪资
    salary = scrapy.Field()

    # 职位链接
    joblink = scrapy.Field()

    # 发布时间
    pub_time = scrapy.Field()

    # 工作经验
    work_exp = scrapy.Field()

    # 学历
    edu = scrapy.Field()

    # 招标人数
    call_num = scrapy.Field()

    # 公司性质（民营|国营）
    company_pro = scrapy.Field()

    # 公司人数
    company_num = scrapy.Field()

    # 职位信息
    job_info = scrapy.Field()

    # 职能类型
    job_type = scrapy.Field()