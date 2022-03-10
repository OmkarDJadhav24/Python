'''
Program Name : Multithreading2.py
Input        : Integer
Output       : Integer
Description  : It is used to display Addition of Even and Odd Factors of Number Using Multithreading 
Author       : Omkar Jadhav
Date         : 8-March-2022
'''


import threading

def chkodd(no):
	list=[]
	ans=0
	for i in range(1,no+1):
		if(no%i)==0:
			list.append(i)
	print("Odd Factors are:",list)
	for no in list:
		if(no%2)==0:
			continue
		else:
			ans=ans+no

	print("Addition of Odd Numbers is:",ans)

def chkeven(no):
	list=[]
	ans=0
	for i in range(2,no+1):
		if(no%i)==0:
			list.append(i)
	print("Even Numbers are:",list)
	for no in list:
		if(no%2)==0:
			ans=ans+no

	print("Addition of Even Factors is:",ans)

def main():
	print("Enter the number")
	no=int(input())

	Evenfactor=threading.Thread(target=chkeven,args=(no,))
	Oddfactor=threading.Thread(target=chkodd,args=(no,))

	Evenfactor.start()
	Oddfactor.start()
	Evenfactor.join()
	Oddfactor.join()

	print("End")

if __name__=="__main__":
	main()