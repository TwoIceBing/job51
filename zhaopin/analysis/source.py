# coding:utf-8
import pandas as pd
import re
from sqlalchemy import create_engine
import matplotlib.pylab as plt

def get_salary(salary):
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

def get_avg_salary(lang='',city=''):
    """
    获取某个编程语言的平均薪资
    :param lang: 编程语言名
    :return: 平均薪资
    """
    jobdf = df[df['jobname'].str.contains(lang)]

    if city != '':
        jobdf = jobdf[jobdf['work_place'].str.contains(city)]
        if jobdf.shape[0] < 10:
            return
    sum_salary = jobdf['salary']

    return sum_salary.astype(float).mean()


def diff_lang():
    """
    获取不同语言的薪资待遇的对比
    :return:
    """

    lang = ['python','java',u'大数据']

    avg_salary = map(get_avg_salary,lang)

    print lang
    print avg_salary

    for i,j in zip(lang,avg_salary):
        print '%s的平均薪资为:%.3fK' % (i.encode('utf-8'),j)

    p = plt.bar(lang,avg_salary)

    autolabel(p)
    plt.xlabel(u'编程语言')
    plt.ylabel(u'平均薪资')
    plt.title(u'python、java、大数据职业薪资待遇对比')
    plt.show()


def autolabel(rects):
    """
    定义函数来显示柱状上的数值
    :param rects:matplotlib.container.BarContainer
    :return:
    """
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x(), 1.01*height, '%.1f' % float(height))


db = create_engine('mysql+pymysql://root:root@localhost:3306/zhaopin?charset=utf8')

df = pd.read_sql_table('job', db)
print df.shape
# (154860, 13)

df = df[df['salary'] != '']
print df.shape
# (148827, 13)

df['salary'] = df['salary'].apply(get_salary)

plt.rcParams['font.sans-serif'] = ['kaiti']
diff_lang()