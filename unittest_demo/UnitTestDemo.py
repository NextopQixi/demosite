#!/bin/python
# coding=utf-8
'''
Created on 2016年3月21日

@author: wujianxin
'''

import time
import unittest


class QA:
    def age(self):
        return 25

    def name(self):
        return 'wujianxin'


class TestQA(unittest.TestCase):
    def setUp(self):
        self.qa = QA()
        print('set up test now')

    def tearDown(self):
        #         time.sleep(2)
        print('tear down case now')

    def test1(self):
        self.assertEqual(self.qa.age(), 25)

    def test2(self):
        self.assertEqual(self.qa.age(), 34)


def ASuite():
    ASuite = unittest.TestSuite()
    ASuite.addTest(QA('test1'))
    ASuite.addTest(QA('test2'))
    return ASuite


if __name__ == '__main__':
    # unittest.main()
    # 通过testsuite执行用例
    runner = unittest.TextTestRunner()
    runner.run(ASuite())
