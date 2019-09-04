#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
import datetime 
def add(path, content):
	with open(path,'a') as f: 
		f.write(content + '\n') 
path = './log.txt' 
now_time = "{}".format(datetime.datetime.now()) 
add(path, now_time)
