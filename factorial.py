'''
Program Name : factorial.py
Input        : Integer
Output       : Integer
Description  : It is used to find factorial of number
Author       : Omkar Jadhav
Date         : 7-March-2022
'''

def fact2(no):
	fact=1
	while(no>0):
		fact=fact*no
		no=no-1
	print(fact)


def fact1(no):
	fact=1

	for i in range(1,no+1):
		fact=fact*i
	print(fact)

def main():
	print("Enter the number:")
	no=int(input())

	fact1(no)
	fact2(no)
	

if __name__=="__main__":
	main()