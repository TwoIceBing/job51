# job51
前程无忧数据分析  
项目树：  
```
│  lpush.py                 （负责从redis推送数据）  
│  run_spider.py            （负责运行爬虫）  
│  scrapy.cfg  
│  
├─analysis  （负责数据分析模块）  
│  │  city_map.py           （将城市的地理位置信息转化为经纬度）  
│  │  cleaning.py           （数据的清洗）  
│  │  job_avg_salary.py     （数据分析）  
│  │  source.py             （数据的本地测试）  
│  │  
│  └─input  （负责存储临时数据文件）  
│          avg_salary.csv   （平均薪资）  
│          city.json        （各职位在不同城市薪资城市）  
│          city_salary.json （城市数据加工处理过后的数据）  
│          read.py          （连接mysql数据库）  
│          test.csv  
│  
├─view  （负责web端的数据展示）  
│  │  main.py               （flask后台代码）  
│  │  __init__.py  
│  │  
│  ├─static （静态文件）  
│  │      echarts.min.js  
│  │      map.html  
│  │      style.css  
│  │  
│  └─templates  （模板文件）  
│          city_salary.html   
│          city_salary2.html  
│          heat_map.html    （热力图展示）  
│          index1.html      （各职位平均薪资条形图展示）  
│          indexjob.html    （各职位在不同城市薪资条形图展示）  
│          job_salary.html    
│          __init__.py    
│  
└─zhaopin   （scrapy爬虫文件）  
    │  items.py             （items文件）  
    │  items.pyc  
    │  log  
    │  middlewares.py       （中间件）  
    │  pipelines.py         （管道）  
    │  pipelines.pyc  
    │  settings.py          （设置）  
    │  settings.pyc  
    │  __init__.py  
    │  __init__.pyc  
    │  
    └─spiders   （爬虫文件）  
            job.py          （爬虫）  
            job.pyc  
            __init__.py  
            __init__.pyc  
  
```
