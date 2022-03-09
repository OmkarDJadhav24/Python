'''
Program Name : filter_map_reduce2.py
Input        : list of Integers
Output       : Integer
Description  : It is used to perform filter map reduce function
Author       : Omkar Jadhav
Date         : 7-March-2022
'''

from functools import reduce

flt=lambda no:no%2==0

map_fun=lambda no:no**2

reduce_fun=lambda a,b:a+b

def main():
	print("How many numbers you want in list:")
	no=int(input())
	data=[]
	print("Enter the elements")
	for i in range(no):
		data.append(int(input()))

	ret1=list(filter(flt,data))
	print("After filter function:",ret1)
	ret2=list(map(map_fun,ret1))
	print("After map function:",ret2)
	ret3=reduce(reduce_fun,ret2)
	print("After reduce function:",ret3)

if __name__=="__main__":
	main()