#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Created on 2016年4月6日

@author: wujianxin
"""
import pymysql
from pymysql.err import MySQLError


def connect(host, user, password, database, port=3306, charset='utf-8'):
    return pymysql.connect(host, user, password, database, port, charset=charset)


def operate(db, sql):
    cursor = db.cursor()
    if sql.find('select') != -1:

        try:
            # 执行查询
            cursor.execute(sql)
            result = cursor.fetchall()
            print(sql, result)
        except MySQLError as e:
            print("Error: select error %d: %s" % (e.args[0], e.args[1]))
    else:
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
            print('opreate success')
        except MySQLError as e:
            # 如果发生错误则回滚
            print("Error: insert error %d: %s" % (e.args[0], e.args[1]))
            db.rollback()


if __name__ == '__main__':
    pass
