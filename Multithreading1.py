'''
Program Name : Multithreading1.py
Input        : Integers
Output       : Integers
Description  : It is used to display Even and Odd Numbers Using Multithreading 
Author       : Omkar Jadhav
Date         : 8-March-2022
'''


import threading

def ChkEven(data):
	list=[]
	for no in data:
		if(no%2)==0:
			list.append(no)

	print("Even Numbers are:",list)

def ChkOdd(data):
	list=[]
	for no in data:
		if(no%2)==0:
			continue
		else:
			list.append(no)

	print("Odd Numbers are:",list)

def main():
	print("Enter the number:")
	no=int(input())

	data=[]
	for i in range(no):
		data.append(int(input()))

	Even=threading.Thread(target=ChkEven,args=(data,))
	Odd=threading.Thread(target=ChkOdd,args=(data,))

	Even.start()
	Odd.start()
	Even.join()
	Odd.join()

if __name__=="__main__":
	main()