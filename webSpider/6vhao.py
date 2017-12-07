'''
Created on 2017年1月3日

@author: wujianxin
'''
import re
import lxml
import urllib.request

totalPage = 0
try:
    url = 'http://www.6vhao.com/dy/'
    response = urllib.request.urlopen(url)
    content = response.read().decode('gbk')
    #     print(content)
    pattern = re.compile('<ul.*?list">(.*?)</ul.*?', re.S)
    items = re.findall(pattern, content)
    print(items)
# print(items)
# for item in items:
except Exception as e:
    #     if hasattr(e, name)
    print(e)
