'''
Program Name : oops1.py
Input        : two Integers
Output       : Integers
Description  : It is used to display values of variables of object 
Author       : Omkar Jadhav
Date         : 8-March-2022
'''

class Demo:
	value=10
	def __init__(self,no1,no2):
		self.no1=no1
		self.no2=no2

	def fun(self):
		print(self.no1)
		print(self.no2)

	def gun(self):
		print(self.no1)
		print(self.no2)

def main():
	obj1=Demo(11,21)
	obj2=Demo(51,101)
	obj1.fun()
	obj1.gun()
	obj2.fun()
	obj2.gun()

if __name__=="__main__":
	main()