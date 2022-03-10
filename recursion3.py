'''
Program Name : recursion3.py
Input        : Integer
Output       : Integers
Description  : It is used to display number patturn in Sequence Using recursion 
Author       : Omkar Jadhav
Date         : 8-March-2022
'''


def Display(no,i):
	if(no>0):
		print(i,end=" ")
		no=no-1
		i=i+1
		Display(no,i)

def main():
	print("Enter the number:")
	no=int(input())

	i=1

	Display(no,i)

if __name__=="__main__":
	main()