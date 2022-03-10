'''
Program Name : Multithreading5.py
Input        : Integer
Output       : Integers
Description  : It is used to display Number in order and in reverse order Using Multithreading 
Author       : Omkar Jadhav
Date         : 8-March-2022
'''


import threading

def Display(no):
	print("In Order")
	for i in range(1,no+1):
		print(i)

def DisplayR(no):
	print("In Reverse Order:")
	for i in range(no,0,-1):
		print(i)

def main():
	print("Enter the number:")
	no=int(input())
	Thread1=threading.Thread(target=Display,args=(no,))
	Thread2=threading.Thread(target=DisplayR,args=(no,))

	Thread1.start()
	Thread1.join()
	Thread2.start()
	Thread2.join()
if __name__=="__main__":
	main()