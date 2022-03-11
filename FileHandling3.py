'''
Program Name : FileHandling3.py
Input        : Names of files
Output       : String
Description  : It is used to copy the contents from one file to another file
Author       : Omkar Jadhav
Date         : 8-March-2022
'''


from sys import argv
def main():
	print("Application Name:",argv[0])

	name_r=argv[1]
	name_w=argv[2]
												
	file_r=open(name_r,"r")										# Existing File for read
	data=file_r.read()

	file_w=open(name_w,"w")										# New file for write
	file_w.write(data)
	file_w.close()
	print("Content wrote successfully in new file")

if __name__=="__main__":
	main()