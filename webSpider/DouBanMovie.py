'''
Created on 2017年1月3日

@author: wujianxin
'''
import re
import urllib.request

subject_id=26325320
# subject_id=2632532035
try:
    url='https://movie.douban.com/subject/' + str(subject_id)
    response=urllib.request.urlopen(url)
    content = response.read().decode('utf-8')
#     print(content)
    pattern = re.compile('<span.*?itemreviewed">(.*?)</span.*?'+'<span.*?year">(.*?)</span.*?'+'<strong.*?average">(.*?)</strong>',re.S)
    items = re.findall(pattern, content)
    print(items)
    # for item in items:
except Exception as e:
#     if hasattr(e, name)
    print(e)
