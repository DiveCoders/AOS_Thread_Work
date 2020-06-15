# !/usr/bin/env python  
# -*- coding:utf8 -*- 
# Author:simonLTS


import time, threading
import math
import time
import random

count = 0
starttime = time.time()


def method(a,b,c):
    if a != 0:
        delta = b**2-4*a*c
        if delta < 0:
            pass
            print("无根")
        elif delta == 0:
            s = -b/(2*a)
            # print("唯一根x=",s)
        else :
            root = math.sqrt(delta)
            x1 = (-b+root)/(2*a)
            x2 = (-b-root)/(2*a)
            # print("x1=",x1,"\t","x2=",x2)


def run_n():
    global count
    global endtime
    while count<1000000:
        # print('thread %s is running...' % threading.current_thread().name)
        a=random.randint(1,100)
        b=random.randint(1,100)
        c=random.randint(1,100)
        method(a,b,c)
        count+=1
        endtime = time.time()
        print(endtime - starttime)


t1 = threading.Thread(target=run_n, args=())
t2 = threading.Thread(target=run_n, args=())


t1.start()
t2.start()

# 66.220787525177
# 82.21578741073608
