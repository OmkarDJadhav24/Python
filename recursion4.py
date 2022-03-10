'''
Program Name : recursion4.py
Input        : Integer
Output       : Integer
Description  : It is used to display Addition of digits of number using Recursion 
Author       : Omkar Jadhav
Date         : 8-March-2022
'''


sum=0

def Display(no):
	global sum
	if(no>0):
		sum=sum+no%10
		no=no//10
		Display(no)
	return sum
def main():
	print("Enter the number:")
	no=int(input())

	ret=Display(no)
	print("Sum of digits of number is:",ret)
if __name__=="__main__":
	main()