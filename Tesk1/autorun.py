# !/usr/bin/env python  
# -*- coding:utf8 -*- 
# Author:simonLTS

# Q3:设计另一个autorun.cpp，它能够将test.exe运行N次（n=10000或100000…）
# 自动收集运行结果存入result.txt文件。

# A3 :结果见result.txt

import os
f=open("result.txt",'a',encoding="utf-8")
n=10
for i in range(n):
	print(i)
	# print(os.system('python ./test.py'))
	f.write(os.popen('python ./test.py').read()+"\n")

