'''
Program Name : patturn1.py
Input        : Integer
Output       : Patturn
Description  : It is used to display the patturn
Author       : Omkar Jadhav
Date         : 7-March-2022
'''

def main():
	print("Enter the number:")
	no=int(input())

	for i in range(no):
		for j in range(no):
			print("*",end=" ")
		print("\r")
if __name__=="__main__":
	main()