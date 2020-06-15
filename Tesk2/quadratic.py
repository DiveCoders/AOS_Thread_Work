# !/usr/bin/env python  
# -*- coding:utf8 -*- 
# Author:simonLTS

import math
import time
import random

def method(a,b,c):
    if a != 0:
        delta = b**2-4*a*c
        if delta < 0:
            print("无根")
        elif delta == 0:
            s = -b/(2*a)
            print("唯一根x=",s)
        else :
            root = math.sqrt(delta)
            x1 = (-b+root)/(2*a)
            x2 = (-b-root)/(2*a)
            print("x1=",x1,"\t","x2=",x2)


def run_n(n):
    starttime = time.time()
    for i in range(n):
        a=random.randint(1,100)
        b=random.randint(1,100)
        c=random.randint(1,100)
        method(a,b,c)
        endtime = time.time()
    print(endtime - starttime)


if __name__ == '__main__': 

    run_n(1000000)
    


