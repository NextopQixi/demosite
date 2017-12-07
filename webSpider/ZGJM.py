'''
Created on 2017年10月31日

@author: wujianxin
'''
import re
import requests
import time
from lib import db_tool

base_url = 'http://www.zgjm.org'


class ZGJM:
    def getPage(self):
        '''获取所有解梦详情页'''
        dream_dict = {}
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        with open('./dream_list.txt', "w+", encoding='utf-8') as f:
            for i in letters:
                url = base_url + "/letterlist/" + i + ".html"
                print(url)
                response = requests.get(url).text
                time.sleep(3)
                pattern = re.compile('<li><a.*?"(.*?)" title="(.*?)"', re.S)
                items = re.findall(pattern, response)
                for item in items:
                    f.write(item[1] + "\t" + base_url + item[0] + '\n')

    def getDreamInfo(self):
        dream_dict = {}
        db = db_tool.connect('59.110.227.223', 'root', 'walle', 'walle', charset="utf8")
        with open('./dream_list.txt', "r", encoding='utf-8') as f:
            for line in f.readlines():
                dream_info = line.split('\t')
                response = requests.get(dream_info[1].strip()).text
                time.sleep(0.2)
                pattern = re.compile('<p>[^·]\s*?\S*?[^：strong>]</p>', re.S)
                items = re.findall(pattern, response)
                content = ''
                for item in items:
                    content += item.replace(u'\u3000', u'').replace("<p>", '').replace("</p>", '')
                dream_dict[dream_info[0]] = content
                sql = 'INSERT INTO dream(title,content) VALUES ("' + dream_info[0] + '","' + content + '");'
                db_tool.operate(db, sql)
        db.close()


if __name__ == '__main__':
    spider = ZGJM()

    # spider.getDreamInfo()
    # print('insert success')
