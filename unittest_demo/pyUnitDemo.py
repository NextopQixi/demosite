#!/bin/python
#coding=utf-8
'''
Created on 2016年3月21日

@author: wujianxin
'''
import unittest
from django.forms.widgets import Widget
class DefaultWidgetSizeTestCase(unittest.TestCase):
    def runTest(self):
        widget = Widget("The widget")
        assert widget.size() == (50,50), 'incorrect default size'
if __name__ == '__main__':
    testCase = DefaultWidgetSizeTestCase()
