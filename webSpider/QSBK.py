'''
Created on 2017年1月3日

@author: wujianxin
'''
import re
import requests
import urllib.request


class QSBK:
    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent}
        self.stories = []
        self.enable = False

    def getPage(self, pageIndex):
        try:
            # url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
            # full_url = urllib.request.Request(url, headers=self.headers)
            # response = urllib.request.urlopen(full_url)
            # content = response.read().decode('utf-8')
            url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
            full_url = urllib.request.Request(url, headers=self.headers)
            response = urllib.request.urlopen(full_url)
            content = response.read().decode('utf-8')
            return content
        except Exception as e:
            print(e)
            return None

    def getPageItems(self, pageIndex):
        content = self.getPage(pageIndex)
        if not content:
            print('页面加载失败')
            return None
        pattern = re.compile('<div.*?clearfix">.*?<h2>(.*?)</h2.*?' + '<div.*?content">.*?<span>(.*?)</span.*?</div>',
                             re.S)
        items = re.findall(pattern, content)
        pageStories = []
        for item in items:
            pageStories.append([item[0].strip(), item[1].strip()])
        return pageStories

    def loadPage(self):
        if self.enable == True:
            if len(self.stories) < 2:
                pageStories = self.getPageItems(self.pageIndex)
                if pageStories:
                    self.stories.append(pageStories)
                    self.pageIndex += 1

    def getOneStory(self, pageStories, page):
        for story in pageStories:
            input_txt = input('')
            self.loadPage()
            if input_txt == 'q':
                self.enable = False
                return
            print(u"第%d页\t发布人:%s\n%s" % (page, story[0], story[1]))

    def start(self):
        print(u"正在读取糗事百科,按回车查看新段子，q退出")
        self.enable = True
        self.loadPage()
        nowPage = 0
        while self.enable:
            if len(self.stories) > 0:
                pageStories = self.stories[0]
                nowPage += 1
                del self.stories[0]
                self.getOneStory(pageStories, nowPage)


if __name__ == '__main__':
    spider = QSBK()
    spider.start()
