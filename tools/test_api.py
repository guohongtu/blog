import threading

import requests
import random
import redis

def getRequest():
    url = "http://127.0.0.1:8000/test_api"
    url2 = "http://127.0.0.1:8888/test_api"
    get_url = random.choice([url, url2])
    # 打开浏览器，输入地址
    requests.get(get_url)


t_list = []
for i in range(30):
    t = threading.Thread(target=getRequest)
    t_list.append(t)
    t.start()

for m in t_list:
    m.join()
