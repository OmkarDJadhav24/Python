'''
Program Name : recursion5.py
Input        : Integer
Output       : Integer
Description  : It is used to display factorial of number Using recursion 
Author       : Omkar Jadhav
Date         : 8-March-2022
'''

answer=1

def Display(no):
	global answer
	if(no>0):
		answer=answer*no
		no=no-1
		Display(no)

	return answer

def main():
	print("Enter the number:")
	no=int(input())

	result=Display(no)
	print("Factorial of Number is:",result)

if __name__=="__main__":
	main()