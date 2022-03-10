'''
Program Name : recursion1.py
Input        : Integer
Output       : Integer
Description  : It is used to display * Using recursion 
Author       : Omkar Jadhav
Date         : 8-March-2022
'''

def fun(no):
	if(no>0):
		print("*",end=" ")
		no=no-1
		fun(no)


def main():
	print("Enter the number:")
	no=int(input())
	
	fun(no)

if __name__=="__main__":
	main()