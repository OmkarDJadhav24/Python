'''
Program Name : Multithreading6.py
Input        : Integer
Output       : Integers
Description  : It is used to display Number in order and in reverse order using lock and Using Multithreading 
Author       : Omkar Jadhav
Date         : 8-March-2022
'''


import threading
import time

def Display(no,lock):
	time.sleep(1)
	lock.acquire()
	print("In Order")
	for i in range(1,no+1):
		print(i)

	lock.release()

def DisplayR(no,lock):
	lock.acquire()
	print("In Reverse Order:")
	for i in range(no,0,-1):
		print(i)

	lock.release()

def main():
	starttime=time.time()
	print("Start Time is:",starttime)
	lock=threading.Lock()
	print("Enter the number:")
	no=int(input())
	Thread1=threading.Thread(target=Display,args=(no,lock))
	Thread2=threading.Thread(target=DisplayR,args=(no,lock))

	Thread1.start()
	time.sleep(1)
	Thread2.start()
	Thread1.join()
	Thread2.join()
	endtime=time.time()

	print("End time is:",endtime)

if __name__=="__main__":
	main()