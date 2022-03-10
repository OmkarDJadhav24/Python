'''
Program Name : lambda_fun2.py
Input        : Two Integers
Output       : Integer
Description  : It is used to multiply two numbers
Author       : Omkar Jadhav
Date         : 7-March-2022
'''

Multiplication=lambda no1,no2:no1*no2

def main():
	no1=int(input("Enter the first name:"))
	no2=int(input("Enter the second name:"))

	ret=Multiplication(no1,no2)
	print("Multiplication is:",ret)

if __name__=="__main__":
	main()