'''
Program Name : FileHandling2.py
Input        : Name of file
Output       : String
Description  : It is used to display the contents of file
Author       : Omkar Jadhav
Date         : 8-March-2022
'''

from sys import argv

def main():
	print("Application Name:",argv[0])

	name=argv[1]

	file=open(name,"r")
	Data=file.read()

	print(Data)

if __name__=="__main__":
	main()