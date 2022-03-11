'''
Program Name : FileHandling1.py
Input        : Path of directory
Output       : String
Description  : It is used to display the path of directory exists or not
Author       : Omkar Jadhav
Date         : 8-March-2022
'''

import os
from sys import argv

def Check_file(name):

	file=os.path.exists(name)

	if(file):
		print("Directory is exist")

def main():
	print("Automation Script Started:")
	print("Name of Application:",argv[0])

	if(len(argv)<2) or (len(argv)>2):
		print("Error:Invalide Number Of Arguments")
		exit()

	elif(argv[1]=='-u' or argv[1]=='-U'):
		print("Usage:Application Name",argv[0])
		exit()

	elif(argv[1]=='-h' or argv[1]=='-H'):
		print("Help:This Script is designed to check file is present or not in current directory")

	name=argv[1]

	Check_file(name)

if __name__=="__main__":
	main()