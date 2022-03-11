'''
Program Name : FileHandling5.py
Input        : Name of file and String
Output       : Integer
Description  : It is used to count frequency of string in file
Author       : Omkar Jadhav
Date         : 8-March-2022
'''

from sys import argv

def main():
	count=0
	print("Application name:",argv[0])

	name=argv[1]
	string=argv[2]
	file=open(name,"r")
	data=file.read()

	count=data.count(string)
	print("Frequency of string in file:",count)

if __name__=="__main__":
	main()