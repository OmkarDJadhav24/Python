'''
Program Name : digit.py
Input        : Integer
Output       : Integer
Description  : It is used for addition of digits of number
Author       : Omkar Jadhav
Date         : 7-March-2022
'''

def main():
	print("Enter the number")
	no=int(input())

	count=0
	while(no>0):
		count=count+no%10
		no=no//10
	print("Addition is:",count)
if __name__=="__main__":
	main()