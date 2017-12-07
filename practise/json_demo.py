#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2016年4月6日

@author: wujianxin
'''

import json


def dict2json():
    # Python 字典类型转换为 JSON 对象
    data = {
        'no': 1,
        'name': 'Runoob',
        'url': 'http://www.runoob.com'
    }

    json_str = json.dumps(data)
    print("Python 原始数据：", repr(data))
    print("JSON 对象：", json_str)


def json2dict():
    data1 = {
        'no': 1,
        'name': 'Runoob',
        'url': 'http://www.runoob.com'
    }

    json_str = json.dumps(data1)
    print("Python 原始数据：", repr(data1))
    print("JSON 对象：", json_str)

    # 将 JSON 对象转换为 Python 字典
    data2 = json.loads(json_str)
    print("data2['name']: ", data2['name'])
    print("data2['url']: ", data2['url'])


def json_file():
    data = {
        'no': 1,
        'name': 'Runoob',
        'url': 'http://www.runoob.com'
    }
    # 写入 JSON 数据
    with open('data.json', 'w') as f:
        json.dump(data, f)

    # 读取数据
    with open('data.json', 'r') as f:
        data = json.load(f)


if __name__ == '__main__':
    dict2json()
    json2dict()
    json_file()
