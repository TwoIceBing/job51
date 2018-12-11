# coding:utf-8
import json
from urllib import urlopen, quote
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

def getlnglat(address):
    url = 'http://api.map.baidu.com/geocoder/v2/'
    output = 'json'
    ak = 'FOtHtZ92dCKMjpx0XA05g8VEZn95QWOK'
    add = quote(address.encode('utf-8')) #由于本文城市变量为中文，为防止乱码，先用quote进行编码
    print add
    uri = url + '?' + 'address=' + add  + '&output=' + output + '&ak=' + ak
    print uri
    req = urlopen(uri)
    res = req.read() #将其他编码的字符串解码成unicode
    temp = json.loads(res) #对json数据进行解析
    return temp

file = open(r'./input/city.json','w') #建立json数据文件
with open(r'./input/city_salary.json', 'r') as f:

    js = json.load(f)

    data = []
    for k,v in js.iteritems():
        c = {}
        c['city'] = k
        c['points'] = []
        for i in range(len(v['city'])):
            if v['city'][i] == u'异地招聘':
                continue
            lnglat = getlnglat(v['city'][i])  # 采用构造的函数来获取经度
            test = {}
            test['lng'] = lnglat['result']['location']['lng']
            test['lat'] = lnglat['result']['location']['lat']
            test['count'] = v['avg_salary'][i]

            c['points'].append(test)
        data.append(c)

    json.dump(data,file,ensure_ascii=False)