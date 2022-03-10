'''
Program Name : Multithreading4.py
Input        : String Value
Output       : Characters
Description  : It is used to display small capital letters with id and name of current thread Using Multithreading 
Author       : Omkar Jadhav
Date         : 8-March-2022
'''


import threading
import os

def chksmall(name):
	list=[]
	for char in name:
		if char.islower()==True:
			list.append(char)
	print('Lower Characters:{} id:{} name:{}'.format(list,os.getpid(),threading.current_thread().name))

def chkcap(name):
	list=[]
	for char in name:
		if char.isupper()==True:
			list.append(char)

	print('Capital Letters:{} id:{} name:{}'.format(list,os.getpid(),threading.current_thread().name))

def chkdigit(name):
	print('digits:{} id:{} name:{}'.format(len(name),os.getpid(),threading.current_thread().name))

def main():
	print("Enter the string:")
	value=input()

	small=threading.Thread(target=chksmall,args=(value,),name="smallthread")
	capital=threading.Thread(target=chkcap,args=(value,),name="capitalthread")
	digit=threading.Thread(target=chkdigit,args=(value,),name="digit")

	small.start()
	capital.start()
	digit.start()
	small.join()
	capital.join()
	digit.join()

if __name__=="__main__":
	main()