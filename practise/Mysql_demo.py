#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2016年4月6日

@author: wujianxin
'''
import pymysql
from pymysql.err import MySQLError

if __name__ == '__main__':
    # 打开数据库连接
    db = pymysql.connect('192.168.217.12', 'root', '123456', 'wjx_test', 7306)

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 使用 execute() 方法执行 SQL，如果表存在则删除
    cursor.execute("DROP TABLE IF EXISTS wjx_test")

    # 使用预处理语句创建表
    sql = """CREATE TABLE wjx_test (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""

    cursor.execute(sql)

    # SQL 插入语句
    sql = """INSERT INTO wjx_test(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except MySQLError as e:
        # 如果发生错误则回滚
        print("Error: insert error %d: %s" % (e.args[0], e.args[1]))
        db.rollback()

    # SQL 插入语句
    sql = "INSERT INTO wjx_test(FIRST_NAME, \
       LAST_NAME, AGE, SEX, INCOME) \
       VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
          ('Mac', 'Mohan', 20, 'M', 2000)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except MySQLError as e:
        # 如果发生错误则回滚
        print("Error: insert error %d: %s" % (e.args[0], e.args[1]))
        db.rollback()

    # 查询语句
    sql = 'select * from wjx_test'
    try:
        # 执行查询
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
    except MySQLError as e:
        print("Error: select error %d: %s" % (e.args[0], e.args[1]))

    # SQL 更新语句
    sql = "UPDATE wjx_test SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except MySQLError as e:
        # 发生错误时回滚
        print("Error: update error %d: %s" % (e.args[0], e.args[1]))
        db.rollback()

    # 查询语句
    sql = 'select * from wjx_test'
    try:
        # 执行查询
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
    except MySQLError as e:
        print("Error: select error %d: %s" % (e.args[0], e.args[1]))
    # 关闭数据库连接
    db.close()
