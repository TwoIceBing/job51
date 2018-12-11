# coding:utf-8
import re
import pandas as pd
from sqlalchemy import create_engine
import json


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
        salary_num = re.search('\d+', salary.split('/')[0]).group()
        money = salary.split('/')[0].strip(salary_num)
    try:
        salary_num = float(salary_num)
    except:
        print salary, '=', money, salary_num
    if time == u'年':
        salary_num = salary_num / 12
    elif time == u'天':
        salary_num *= 30.
    elif time == u'小时':
        salary_num *= 30 * 12
    if money == u'万':
        salary_num *= 10
    elif money == u'元':
        salary_num /= 1000

    return salary_num


def get_avg_salary(lang='', city=''):
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

    lang = ['python', 'java', u'大数据']

    avg_salary = map(get_avg_salary, lang)

    print lang
    print avg_salary

    f = open('./input/avg_salary.csv', 'w')
    for i, j in zip(lang, avg_salary):
        f.write('%s,%.3f\n' % (i.encode('utf-8'), j))
        print '%s的平均薪资为:%.3fK' % (i.encode('utf-8'), j)
    f.close()


def diff_place():
    """
    获取同一语言不通地区薪资的待遇
    :return:
    """

    citys = list(df['work_place'].str.split('-').map(lambda x: x[0]).drop_duplicates())

    citys.remove(u'朝阳')
    # 朝阳有点特殊，有些城市直接就是朝阳，不过数量太少，直接忽略了，所以这里做朝阳的特殊处理

    lang = ['python', 'java', u'大数据']

    # ls如：['python','北京']
    ls = [[a, b] for a in lang for b in citys]

    # x是某种语言在某个城市的平均薪资
    x = [get_avg_salary(*l) for l in ls]

    info = {}

    for i, j in zip(ls, x):
        # if j != None:
        #     print i[0],i[1],j
        if not info.has_key(i[0]):
            info[i[0]] = {}
            info[i[0]]['city'] = []
            info[i[0]]['avg_salary'] = []
        if j != None:
            info[i[0]]['city'] += [i[1]]
            info[i[0]]['avg_salary'] += [j]

    # info的可能取值如：info = {"python": {"city": ["上海", "成都",...],"avg_salary": [11.974358974358974, 7.016129032258065, ...]},...}

    with open('./input/city_salary.json', 'w') as inf:
        json.dump(info, inf)


if __name__ == '__main__':
    db = create_engine('mysql+pymysql://root:root@localhost:3306/zhaopin?charset=utf8')

    df = pd.read_sql_table('job', db)
    print df.shape
    # (154860, 13)

    df = df[df['salary'] != '']
    print df.shape
    # (148827, 13)

    df['salary'] = df['salary'].apply(get_format_salary)

    # 获取不同语言的薪资待遇的对比
    # diff_lang()

    # 同一语言不同地区薪资的待遇
    diff_place()
