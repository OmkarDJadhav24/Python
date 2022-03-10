'''
Program Name : factorial2.py
Input        : Integer
Output       : Integer
Description  : It is used to find factorial of number
Author       : Omkar Jadhav
Date         : 7-March-2022
'''

def main():
	print("Enter the number:")
	no=int(input())
	fact=0
	while(no>0):
		fact=fact+no
		no=no-1
	print(fact)
if __name__=="__main__":
	main()