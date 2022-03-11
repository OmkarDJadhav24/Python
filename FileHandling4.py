'''
Program Name : FileHandling4.py
Input        : names of files
Output       : String
Description  : It is used to check the contents of two files are same
Author       : Omkar Jadhav
Date         : 8-March-2022
'''


from sys import argv

def main():
	print("Application Name:",argv[0])

	name1=argv[1]
	name2=argv[2]

	file1=open(name1,"r")
	data1=file1.read()

	file2=open(name2,"r")
	data2=file2.read()

	res=""
	for i in data1:
		if i in data2 and not i in res:
			res=res+i

	print(res)
if __name__=="__main__":
	main()