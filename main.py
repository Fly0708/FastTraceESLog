import os
import sys
import uuid

from elasticsearch7 import Elasticsearch
from configparser import ConfigParser

# 创建 ConfigParser 对象
config = ConfigParser()

# 读取 properties 文件
config.read('config.properties')

# 建立 Elasticsearch 客户端连接
es = Elasticsearch([config.get('default', 'es.url')],
                   http_auth=(config.get('default', 'es.username'), config.get('default', 'es.password')))
# 构建查询
query = {
    "match": {
        "message": sys.argv[1]
    }
}

sort = [
    {
        "start_time": {
            "order": "asc"
        }
    }
]

# 发送查询请求
response = es.search(index="filebeat*", query=query, sort=sort,size= 500)

messages = [hit["_source"]['message'] for hit in response["hits"]["hits"]]

# write messages to file
random_log_file = config.get('default', 'random.log.file.path')
log_file = os.path.join(random_log_file, '{}.log'.format(str(uuid.uuid4())))

messages = [message + '\n' for message in messages]
with open(log_file, "w", encoding='utf-8') as f:
    f.writelines(messages)

#  notepad open messages.txt
os.system("atom {}".format(log_file))
