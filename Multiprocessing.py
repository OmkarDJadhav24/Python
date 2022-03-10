'''
Program Name : Multiprocessing.py
Input        : Integer
Output       : Integers
Description  : It is used to display Number in order and in reverse order using lock and Using Multiprocessing 
Author       : Omkar Jadhav
Date         : 8-March-2022
'''


import multiprocessing

def Display(no,lock):
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
	lock=multiprocessing.Lock()

	no=int(input("Enter the number:"))
	
	p1=multiprocessing.Process(target=Display,args=(no,lock))
	p2=multiprocessing.Process(target=DisplayR,args=(no,lock))

	p1.start()
	p2.start()
	p1.join()
	p2.join()
if __name__=="__main__":
	main()