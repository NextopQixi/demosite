#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2016年4月6日

@author: wujianxin
'''
import sys
#Python 3.3开始ElementTree模块会自动寻找可用的C库来加快速度，所以只需要import xml.etree.ElementTree就可以
try: 
    import xml.etree.cElementTree as ET 
except ImportError: 
    import xml.etree.ElementTree as ET 
  
# from xml.dom.minidom import parse 
import xml.dom.minidom 

import xml.sax


def ET_analysis():
    try:
        tree = ET.parse('country.xml')
        root = tree.getroot()
    # 2.x Exception,e;3.x Exception as e
    except Exception as e:
        print('Error:cannot parse file:country.xml. errmsg:',e.value)
        sys.exit(1)
    print(root.tag,'----',root.attrib)
    for child in root: 
        print(child.tag, "---", child.attrib)
    print("*"*10)
    print(root[0][1].text)   #通过下标访问 
    print(root[0].tag, root[0].text) 
    print("*"*10)
      
    for country in root.findall('country'): #找到root节点下的所有country节点 
        rank = country.find('rank').text   #子节点下节点rank的值 
        name = country.get('name')      #子节点下属性name的值 
        print(name, rank)
         
    #修改xml文件 
    for country in root.findall('country'):
        rank = int(country.find('rank').text) 
        if rank > 50: 
            root.remove(country) 
      
    tree.write('./output.xml')  

def DOM_analysis():
    # 使用minidom解析器打开XML文档 
    DOMTree = xml.dom.minidom.parse("country.xml") 
    Data = DOMTree.documentElement 
    if Data.hasAttribute("name"): 
        print("name element : %s" % Data.getAttribute("name")) 
  
    # 在集合中获取所有国家 
    Countrys = Data.getElementsByTagName("country") 
  
    # 打印每个国家的详细信息 
    for Country in Countrys: 
        print("*****Country*****")
        if Country.hasAttribute("name"): 
            print("name: %s" % Country.getAttribute("name"))
  
        rank = Country.getElementsByTagName('rank')[0] 
        print("rank: %s" % rank.childNodes[0].data )
        year = Country.getElementsByTagName('year')[0] 
        print("year: %s" % year.childNodes[0].data )
        gdppc = Country.getElementsByTagName('gdppc')[0] 
        print("gdppc: %s" % gdppc.childNodes[0].data) 
  
        for neighbor in Country.getElementsByTagName("neighbor"):  
            print(neighbor.tagName, ":", neighbor.getAttribute("name"), neighbor.getAttribute("direction"))

class CountryHandler(xml.sax.ContentHandler): 
    def __init__(self): 
        self.CurrentData = "" 
        self.rank = "" 
        self.year = "" 
        self.gdppc = "" 
        self.neighborname = "" 
        self.neighbordirection = "" 
  
        # 元素开始事件处理 
    def startElement(self, tag, attributes): 
        self.CurrentData = tag 
        if tag == "country": 
            print("*****Country*****")
            name = attributes["name"] 
            print("name:", name) 
        elif tag == "neighbor": 
            name = attributes["name"] 
            direction = attributes["direction"] 
            print(name, "->", direction )
  
    # 元素结束事件处理 
    def endElement(self, tag): 
        if self.CurrentData == "rank": 
            print("rank:", self.rank)
        elif self.CurrentData == "year": 
            print("year:", self.year) 
        elif self.CurrentData == "gdppc": 
            print("gdppc:", self.gdppc) 
        self.CurrentData = "" 
  
    # 内容事件处理 
    def characters(self, content): 
        if self.CurrentData == "rank": 
            self.rank = content 
        elif self.CurrentData == "year": 
            self.year = content 
        elif self.CurrentData == "gdppc": 
            self.gdppc = content 

def SAX_analysis():
    # 创建一个 XMLReader 
    parser = xml.sax.make_parser() 
    # turn off namepsaces 
    parser.setFeature(xml.sax.handler.feature_namespaces, 0) 
  
    # 重写 ContextHandler 
    Handler = CountryHandler() 
    parser.setContentHandler(Handler) 
    
    parser.parse("country.xml") 
    
    
if __name__ == '__main__':
#     ET_analysis()
    DOM_analysis()
#     SAX_analysis()
    
    