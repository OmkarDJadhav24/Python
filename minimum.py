'''
Program Name : minimum.py
Input        : List of Integers
Output       : Integer
Description  : It is used to minimum element of list
Author       : Omkar Jadhav
Date         : 7-March-2022
'''

def sort_fun(list):
	for i in range(len(list)-1):
		for j in range(len(list)-1):
			if(list[j]>list[j+1]):
				list[j],list[j+1]=list[j+1],list[j]      				#swapping

	print("Sorted list is:",list)
	print("Minimum element from list is:",list[0])
	
def main():
	print("Enter the number")
	no=int(input())
	
	list=[]
	
	print("Enter the elements")
	
	for i in range(no):
		list.append(int(input()))

	print(list)

	sort_fun(list)

if __name__=="__main__":
	main()