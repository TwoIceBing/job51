# coding:utf-8
import re

def get_format_salary(salary):
    """
    将薪资格式化
    :param salary:薪资，如：1-1.5万/月
    :return: 10K
    """
    time = salary.split('/')[1]
    if salary.__contains__('-'):
        money = salary.split('/')[0][-1]
        salary_num = salary.split('-')[0]
    else:
        salary_num = re.search('\d+',salary.split('/')[0]).group()
        money = salary.split('/')[0].strip(salary_num)
    try:
        salary_num = float(salary_num)
    except:
        print salary,'=',money,salary_num
    if time == u'年':
        salary_num = salary_num/12
    elif time == u'天':
        salary_num *= 30.
    elif time == u'小时':
        salary_num *= 30*12
    if money == u'万':
        salary_num *= 10
    elif money == u'元':
        salary_num /= 1000

    return salary_num


