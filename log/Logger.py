#!/bin/bash
#coding=utf-8
'''
Created on 2016年3月21日

@author: wujianxin
'''

import logging
import logging.config

logging.config.fileConfig("logger.conf")
logger = logging.getLogger("example01")

logger.debug('This is debug message')
logger.info('This is info message')
logger.warning('This is warning message')