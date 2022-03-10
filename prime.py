'''
Program Name : prime.py
Input        : Integer
Output       : String
Description  : It is used to check number is prime or not
Author       : Omkar Jadhav
Date         : 7-March-2022
'''


def prime(no):
	fact=True
	for i in range(2,no):
		if(no%i==0):
			print("This is not a prime number")
			break
		
	else:
		print("This is prime number")
def main():
	print("Enter the number")
	no=int(input())

	prime(no)
if __name__=="__main__":
	main()