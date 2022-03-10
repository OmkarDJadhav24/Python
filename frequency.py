'''
Program Name : frequency.py
Input        : List of Integers
Output       : Integer
Description  : It is used to find frequency of maximum times occured number
Author       : Omkar Jadhav
Date         : 7-March-2022
'''

def freq_fun(list,value):
	count=0
	for no in list:
		if(no==value):
			count=count+1

	return count

def main():
	print("Enter the number you want to load in list")
	no=int(input())

	list=[]

	print("Enter the elements:")
	for i in range(no):
		list.append(int(input()))

	print("Enter the number to search frequency")
	no1=int(input())

	result=freq_fun(list,no1)
	print("Frequency of the number is:",result)

if __name__=="__main__":
	main()