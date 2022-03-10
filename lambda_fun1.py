'''
Program Name : lambda_fun1.py
Input        : Integer
Output       : Integer
Description  : It is used to find Square of Number
Author       : Omkar Jadhav
Date         : 7-March-2022
'''

pow_two=lambda no:no**2

def main():
	print("Enter the number")
	no=int(input())

	ret=pow_two(no)
	print("Square of number is:",ret)

if __name__=="__main__":
	main()