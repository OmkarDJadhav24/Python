'''
Program Name : filter_map_reduce1.py
Input        : list of Integers
Output       : Integer
Description  : It is used to perform filter map reduce function
Author       : Omkar Jadhav
Date         : 7-March-2022
'''

from functools import reduce

filter_out=lambda no:(no>=70 and no<=90)

increase=lambda no:no+10

Product_fun=lambda a,b:a*b

def main():
	print("How many numbers you want in list:")
	no=int(input())
	data=[]
	print("Enter the elements")
	for i in range(no):
		data.append(int(input()))

	ret1=list(filter(filter_out,data))
	print("After filter function:",ret1)
	ret2=list(map(increase,ret1))
	print("After map function:",ret2)
	ret3=reduce(Product_fun,ret2)
	print("After reduce function:",ret3)

if __name__=="__main__":
	main()