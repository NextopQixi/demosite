#!/usr/bin/python
#coding=utf-8
'''
Created on 2016年4月25日

@author: wujianxin
'''

import re
import logging
import urllib.request
from collections import deque

queue = deque()
visited = set()

url = 'http://news.dbanotes.net'  # 入口页面, 可以换成别的
 
queue.append(url)
cnt = 0

resource = open("./resource.txt", 'w+')

while queue:
    url = queue.popleft()  # 队首元素出队
    visited |= {url}  # 标记为已访问
 
    print('已经抓取: ' + str(cnt) + '   正在抓取 <---  ' + url)
    resource.write('已经抓取: ' + str(cnt) + '   正在抓取 <---  ' + url + '\n')
    cnt += 1
    try:
        urlop = urllib.request.urlopen(url)
        if 'html' not in urlop.getheader('Content-Type'):
            continue
    except Exception:
        logging.error("bad request,url:"+ url)
 
    # 避免程序异常中止, 用try..catch处理异常
    try:
        data = urlop.read().decode('utf-8')
    except:
        continue
 
    # 正则表达式提取页面中所有队列, 并判断是否已经访问过, 然后加入待爬队列
    linkre = re.compile('href=\"(.+?)\"')
    for x in linkre.findall(data):
        if 'http' in x and x not in visited:
            queue.append(x)
            print('加入队列 --->  ' + x)
            resource.write('加入队列 --->  ' + x + '\n')
resource.close()            
            