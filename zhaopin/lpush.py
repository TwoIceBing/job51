# coding:utf-8
import redis

redis_cli=redis.Redis(host='192.168.1.102',password=123, port=6379, db=0)

redis_cli.lpush("Job:job",'java')
redis_cli.lpush("Job:job",'python')
redis_cli.lpush("Job:job",'大数据')
