# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider
from ..items import ZhaopinItem
# from zhaoping.items import ZhaopinItem


class JobSpider(RedisCrawlSpider):
    name = 'job'
    allowed_domains = ['51job.com']
    # start_urls = ['http://51job.com/']

    redis_key = "Job:job"
    start_url = "https://search.51job.com/list/000000,000000,0000,00,9,99,%s,2,%d.html"

    rules = (
        Rule(   # 爬取的页码规则
            LinkExtractor(
                allow=r'https://search.51job.com/list/000000,000000,0000,00,9,99,.+?,2,\d+?.html',  # 爬取规则
                process_value=lambda x: (x.split('.html')[0] + ".html"),    # 链接处理
                restrict_xpaths=("//div[@class='p_in']")    #爬取所处域，由xpath定位
            ),
            callback='parse_item',
            follow=True,
        ),
        # Rule(   # 爬取的职位规则
        #     LinkExtractor(
        #         allow=r'https://jobs.51job.com/.+?/\d+?.html?s=01&t=0',  # 爬取规则
        #         restrict_xpaths=("//div[@class='el']")  # 爬取所处域，由xpath定位
        #     ),
        #     callback='job_item',
        #     follow=True,
        # ),
    )

    def make_request_from_data(self, data):
        """
        重写父类，对redis push过来的值进行处理，形成一个url
        :param data: job名，如:java
        :return: 同父类的返回值
        """
        if '://' in data:
            return self.make_requests_from_url(data)
        else:
            url = self.start_url%(data,1)
            self.logger.info("解析后的url为: %s", url)
            return self.make_requests_from_url(url)

    def parse_item(self, response):
        """
        解析职位信息，包括职位名、公司名、工作地点、薪资以及需要跟进的链接
        :param response:
        :return:
        """
        ajob = response.xpath('//div[@id="resultList"]/div[@class="el"]')

        for job in ajob:
            item = ZhaopinItem()

            item['jobname'] = ''.join(job.xpath('./p/span/a/@title').extract())

            item['company'] = ''.join(job.xpath('./span[1]/a/text()').extract())

            item['work_place'] = ''.join(job.xpath('./span[2]/text()').extract())

            item['salary'] = ''.join(job.xpath('./span[3]/text()').extract())

            item['pub_time'] = ''.join(job.xpath('./span[4]/text()').extract())

            item['joblink'] = ''.join(job.xpath('./p/span/a/@href').extract())

            # 使用''.join(l)替换l[0]是为了让列表数据为空时也不报错

            yield scrapy.Request(item['joblink'],meta={'item':item},callback=self.parse_job)

    def parse_job(self,response):
        """
        解析职位的详细信息，包括职位信息
        :param response:
        :return:
        """
        item = response.meta['item']
        work_info = response.xpath('//p[@class="msg ltype"]/text()').extract()
        item['work_exp'] = work_info[1].strip()
        item['edu'] = work_info[2].strip()
        item['call_num'] = work_info[3].strip()

        company = response.xpath('//p[@class="at"]/text()').extract()
        item['company_pro'] = company[0].strip()
        item['company_num'] = company[1].strip()

        item['job_info'] = ''.join(response.xpath('//div[@class="bmsg job_msg inbox"]/p/text()').extract())
        item['job_type'] = ''.join(response.xpath('//div[@class="bmsg job_msg inbox"]/div[@class="mt10"]/p[1]/a/text()').extract()).split()[0]
        print(item['job_type'])
        yield item


