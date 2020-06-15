# !/usr/bin/env python  
# -*- coding:utf8 -*- 
# Author:simonLTS

# Q4:是否可以消除test.exe多次运行时其结果的不一致性？请给出解决方案，测试其可行性。
# A4：可以消除，使用线程锁，实现如下。

import time, threading

sum = 0
lock = threading.Lock()

def thread_T1(n):

	global sum
	while True:
		lock.acquire()
		if sum<n:
			sum+=1
			
		else:
			print('sum1=',sum)
			break
		lock.release()

def thread_T2(n):

	global sum
	while True:
		lock.acquire()
		if sum<n:
			sum+=2
			
		else:
			print('sum2=',sum)
			break
		lock.release()


t1 = threading.Thread(target=thread_T1, args=(1000000,))
t2 = threading.Thread(target=thread_T2, args=(1000000,))

t1.start()
t2.start()


