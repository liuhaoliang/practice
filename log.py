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
    os.system(r"git add . && sleep 2s && git commit -m sss && sleep 2s && git push")


timer = threading.Timer(20, fun_timer)
timer.start()
