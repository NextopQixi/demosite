#!/usr/bin/python
# coding=utf-8
'''
Created on 2016年4月5日

@author: wujianxin
'''
import os

# python 3.4 无raw_input函数
str = input("请输入：");
print("你输入的内容是: ", str)

# 打开一个文件
fo = open("foo.txt", "w+")
print("文件名: ", fo.name)
print("是否已关闭 : ", fo.closed)
print("访问模式 : ", fo.mode)
# pthon 3.4 file对象无softspace
# print("末尾是否强制加空格 : ", fo.softspace)
fo.write(str)
# 查找当前位置
position = fo.tell();
print("当前文件位置 : ", position)
# 把指针再次重新定位到文件开头
position = fo.seek(0, 0);
print("当前文件位置 : ", position)
aa = fo.read(10)
print('读取的内容为', aa)
fo.close()

# os.rename(current_file_name, new_file_name)
# os.remove(file_name)
# os.mkdir("newdir")
# os.chdir("newdir")
# os.getcwd()
# os.rmdir('dirname')
