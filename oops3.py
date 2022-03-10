'''
Program Name : oops3.py
Input        : two Integers
Output       : Integers
Description  : It is used to perform Addition Substraction Division Multiplication 
Author       : Omkar Jadhav
Date         : 8-March-2022
'''


class Arithmetic:
	def __init__(self):
		self.value1=0
		self.value2=0

	def Accept(self):
		self.value1=int(input("Enter the first number:"))
		self.value2=int(input("Enter the second number:"))

	def Addition(self):
		ret=0
		ret=self.value1+self.value2
		return ret

	def Substraction(self):
		ret=0
		ret=self.value1-self.value2
		return ret

	def Multiplication(self):
		ret=0
		ret=self.value1 * self.value2
		return ret

	def Division(self):
		ret=0
		ret=self.value1/self.value2
		return ret

def main():
	obj=Arithmetic()
	obj.Accept()
	Result1=obj.Addition()
	Result2=obj.Substraction()
	Result3=obj.Multiplication()
	Result4=obj.Division()

	print("Addition is:",Result1)
	print("Substraction is:",Result2)
	print("Multiplication is:",Result3)
	print("Division is:",Result4)

if __name__=="__main__":
	main()