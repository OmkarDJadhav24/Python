'''
Program Name : recursion2.py
Input        : Integer
Output       : Integers
Description  : It is used to display reverse number patturn Using recursion 
Author       : Omkar Jadhav
Date         : 8-March-2022
'''


def Display(no):
	if(no>0):
		print(no,end=" ")
		no=no-1
		Display(no)

def main():
	print("Enter the name:")
	no=int(input())

	Display(no)

if __name__=="__main__":
	main()