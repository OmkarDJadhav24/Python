'''
Program Name : createtxtfile.py
Input        : String Value
Description  : It is used to create text file and write contents in it
Author       : Omkar Jadhav
Date         : 8-March-2022
'''

import os

def main():
	print("Enter the name of file to create:")
	name=input()

	file=open(name,"x")
	file=open(name,"w")
	
	data=input("Enter the Content to write in file:")

	file.write(data)
	file.close()

if __name__=="__main__":
	main()