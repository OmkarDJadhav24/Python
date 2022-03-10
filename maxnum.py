'''
Program Name : maximum.py
Input        : List of Integers
Output       : Integer
Description  : It is used to find maximum number from list
Author       : Omkar Jadhav
Date         : 7-March-2022
'''


def sort_values(list):
	for i in range(len(list)-1):
		for j in range(len(list)-1):
			if(list[j]>list[j+1]):
				list[j],list[j+1]=list[j+1],list[j]
	print(list)
	print("Using user define sort function maximum value is:",list[-1])

def main():
	print("Enter the number:")
	no=int(input())
	list=[]
	print("Enter the elements")
	for i in range(no):
		list.append(int(input()))
	print("Elements in list:",list)

	new_list=sorted(list)
	print(new_list)
	print("Using inbuilt sort function maximum value is:",new_list[-1])
	sort_values(list)

if __name__=="__main__":
	main()