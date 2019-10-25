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
    print(now_time)
    add(path, now_time)
    os.system(r"py log.py && git add . && git commit -m sss && git push")


timer = threading.Timer(60*60, fun_timer)
timer.start()
