'''
Program Name : patturn3.py
Input        : Integer
Output       : Patturn
Description  : It is used to display the patturn
Author       : Omkar Jadhav
Date         : 7-March-2022
'''


def main():
	print("Enter the number")
	no=int(input())

	for i in range(1,no+1):
		for j in range(1,i+1):
			print(j,end="  ")
		print("\r")

if __name__=="__main__":
	main()