#!/bin/python
#coding=utf-8
'''
Created on 2016年3月21日

@author: wujianxin
'''
try:
    fh = open("testfile", "w")
    fh.write("This is my test file for exception handling!!")
except IOError:
    print("Error: can\'t find file or read data")
else:
    print("Written content in the file successfully")
    fh.close()