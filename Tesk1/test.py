# !/usr/bin/env python  
# -*- coding:utf8 -*- 
# Author:simonLTS

# Q1
# 1.设计一个test.cpp，定义变量：unsigned int sum=0;创建2个线程T1和T2， 
# T1的行为：sum+=1；T2的行为： sum+=2；当sum大于1000000时，输出sum的值，程序结束。

# A1
# 0
# sum2= 1000001
# sum1= 1000001

# -----------------------------------

# Q2:10次运行结果是否一致？若不一致，请解释原因。

# A2
# 不一致

# 原因：高级语言中，一条语句在CPU执行时是若干条语句，并且多线程中，所有变量都由所有线程共享，所以，
# 任何一个变量都可以被任何一个线程修改，因此
# 线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。

import time, threading

sum = 0

def thread_T1(n):

	global sum
	while True:
		if sum<n:
			sum+=1
		else:
			print('sum1=',sum)
			break

def thread_T2(n):

	global sum
	while True:
		if sum<n:
			sum+=2
		else:
			print('sum2=',sum)
			break

t1 = threading.Thread(target=thread_T1, args=(1000000,))
t2 = threading.Thread(target=thread_T2, args=(1000000,))

t1.start()
t2.start()

# 结果：
# 0
# sum2= 1000001
# sum1= 1000001
# 1
# sum2= 1000001
# sum1= 1000000
# 2
# sum2= 1000000
# sum1= 1000000
# 3
# sum2= 1000001
# sum1= 1000001
# 4
# sum1= 1000000
# sum2= 1000001
# 5
# sum2= 1000001
# sum1= 1000001
# 6
# sum2= 1000000
# sum1= 1000001
# 7
# sum2= 1000001
# sum1= 1000000
# 8
# sum2= 1000001
# sum1= 1000000
# 9
# sum2= 1000000
# sum1= 1000000


