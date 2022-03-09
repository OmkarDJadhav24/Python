'''
Program Name : filter_map_reduce.py
Input        : list of Integers
Output       : Integer
Description  : It is used to perform filter map reduce function
Author       : Omkar Jadhav
Date         : 7-March-2022
'''

from functools import reduce

def flt_fun(no):
	Flag=False
	for i in range(2,no):
		if(no%i)==0:
			Flag=True
	if(Flag==False):
		return no

def map_fun(no):
	return no*2

def reduce_fun(a,b):
	if(a>b):
		return a
	else:
		return b

def main():
	print("how many elements you want in list:")
	no=int(input())

	data=[]

	print("Enter the elements")
	for i in range(no):
		data.append(int(input()))

	ret1=list(filter(flt_fun,data))
	print(ret1)
	ret2=list(map(map_fun,ret1))
	print(ret2)
	ret3=reduce(reduce_fun,ret2)
	print(ret3)

if __name__=="__main__":
	main()