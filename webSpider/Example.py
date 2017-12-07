'''
Created on 2017年11月4日

@author: wujianxin
'''
import datetime
import re
import time
import itertools
import requests
import lxml.html
from urllib import robotparser
from urllib.parse import urlparse
from bs4 import BeautifulSoup


def download(url, user_agent='wswp', retry=2):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36'
    print("Downloading:", url)
    # 请求header &代理
    headers = {"User-agent": user_agent}
    # proxies = { "http": "http://10.10.1.10:3128", "https": "http://10.10.1.10:1080", }
    proxies = None
    try:
        html = requests.get(url, headers=headers, proxies=proxies)
    except Exception as e:
        print("Download error:", e.reason)
        html = None
        if retry > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return download(url, retry - 1)
    return html.text


# 正则匹配下载指定内容
def crawl_sitemap(url):
    sitemap = download(url)
    links = re.findall('<loc>(.*?)</loc>', sitemap)
    for link in links:
        html = download(link)
        print(html)


# 根据自增id下载网页，最大连续错误5次
def id_iter(url):
    max_errors = 5
    num_errors = 0
    for page in itertools.count(1):
        target_url = url + str(page)
        html = download(target_url)
        if html is None:
            num_errors += 1
            if num_errors == max_errors:
                break
        else:
            num_errors = 0
            pass


def link_crawler(seed_url, link_regex, max_depth=2, delay=3):
    crawl_queue = [seed_url]
    throttle = Throttle(delay)
    seen = {}
    if not can_fetch(seed_url):
        print("%s is blocked by robots.txt" % seed_url)
        return "%s is blocked by robots.txt" % seed_url
    while crawl_queue:
        target_url = crawl_queue.pop()
        depth = seen[target_url]
        if depth == max_depth:
            return 'err: max depth'
        throttle.wait(target_url)
        html = download(target_url)
        for link in get_link(html.text):
            if re.match(link_regex, link):
                com_url = seed_url + link
                if com_url not in seen:
                    seen[com_url] = depth + 1
                    crawl_queue.append(com_url)


def get_link(html):
    web_page_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    return web_page_regex.findall(html)


# 检查robots.txt查看是否可爬
def can_fetch(url):
    rp = robotparser.RobotFileParser()
    rp.set_url(url + 'robots.txt')
    rp.read()
    user_agent = 'BadCrawler'
    return rp.can_fetch(user_agent, url)


# 通过正则获取网页数据
def get_data_re():
    url = 'http://www.zgjm.org/letterlist/A.html'
    html = download(url)
    print(re.findall('<li><a.*?"(.*?)" title="(.*?)"', html))


# 通过beautifulsoup获取网页数据
def get_data_bf():
    url = 'http://www.zgjm.org/letterlist/A.html'
    html = download(url)
    soup = BeautifulSoup(html, 'html.parser')
    list_div = soup.find('div', attrs={'id': 'list'})
    print(list_div)


# 通过lxml获取网页数据
def get_data_lxml():
    url = 'http://www.zgjm.org/letterlist/B.html'
    html = download(url)
    tree = lxml.html.fromstring(html)
    # css选择器
    link_list = tree.cssselect('div#list a')
    for i in link_list:
        print(i.attrib, i.text_content())


class Throttle:

    '''下载限速设置'''

    def __init__(self, delay):
        self.delay = delay
        self.domains = {}

    def wait(self, url):
        domain = urlparse(url).netloc
        last_accessed = self.domains.get(domain)
        if self.delay > 0 and last_accessed is not None:
            sleep_secs = self.delay - (datetime.datetime.now() - last_accessed).seconds
            if sleep_secs > 0:
                time.sleep(sleep_secs)
        self.domains[domain] = datetime.datetime.now()


if __name__ == "__main__":
    url = "http://www.zgjm.org/"
    # get_data_lxml()
    # link_crawler(url, "/.*?(index|view)")
    # print(response.text)
    print(urlparse(url).netloc)
