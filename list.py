'''
Function Name: Addition
Input        : List of Integers
Output       : Integer
Description  : It is used to perform addition of elements of list
Author       : Omkar Jadhav
Date         : 7-March-2022
'''
def Addition(list):
	ans=0
	for no in list:
		ans=ans+no
	return ans

def main():
	print("Enter the number")
	no=int(input())
	list=[]
	print("Enter the elements:")
	for i in range(no):
		list.append(int(input()))

	print("Elements in list:",list)
	result=Addition(list)
	print("Addition is:",result)

if __name__=="__main__":
	main()