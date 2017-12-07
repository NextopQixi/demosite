#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2016年4月6日

@author: wujianxin
'''
import threading
import time 
def music(func):
    while True:
        print("I was listening to %s. %s" %(func,time.ctime()))
        time.sleep(2)

def move(func):
    while True:
        print("I was watching movie named %s! %s" %(func,time.ctime()))
        time.sleep(5)

threads = []
t1 = threading.Thread(target=music,args=(u'爱情买卖',))
threads.append(t1)
t2 = threading.Thread(target=move,args=(u'阿凡达',))
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        '主线程不管子线程是否完成，直接退出'
#         t.setDaemon(True)
        t.start()
        t.join(15)

#     print("all over %s" %ctime())