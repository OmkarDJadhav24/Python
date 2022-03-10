'''
Program Name : Multithreading3.py
Input        : Integers
Output       : Integers
Description  : It is used to display Addition of Even and Odd Numbers of List Using Multithreading 
Author       : Omkar Jadhav
Date         : 8-March-2022
'''


import threading

def chkodd(list):
	data=[]
	ans=0
	for no in list:
		if(no%2)==0:
			continue
		else:
			data.append(no)

	print("Odd Numbers are:",data)
	for no in data:
		ans=ans+no

	print("Addition of Odd Numbers is:",ans)
def chkeven(list):
	data=[]
	ans=0
	for no in list:
		if(no%2)==0:
			data.append(no)
	print("Even Numbers are:",data)

	for no in data:
		ans=ans+no

	print("Addition of Even Numbers is:",ans)
def main():
	print("Enter the number:")
	no=int(input())
	list=[]
	print("Enter the numbers:")
	for i in range(no):
		list.append(int(input()))

	Evenlist=threading.Thread(target=chkeven,args=(list,))
	Oddlist=threading.Thread(target=chkodd,args=(list,))

	Evenlist.start()
	Oddlist.start()
	Evenlist.join()
	Oddlist.join()

if __name__=="__main__":
	main()