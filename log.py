#!/usr/bin/env python
# -*- coding:utf-8 -*-
import datetime
import os
import threading

path = './log.txt'


def add(path, content):
    with open(path, 'a') as f:
        f.write(content + '\n')


def fun_timer():
    now_time = "{}".format(datetime.datetime.now())
    print('hello timer')
    add(path, now_time)
    log = os.system(r"py log.py && git add . && git commit -m sss && git push")


timer = threading.Timer(6, fun_timer)  # 首次启动
timer.start()
