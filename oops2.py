'''
Program Name : oops2.py
Input        : Integer
Output       : Integer and Float
Description  : It is used to display Radius Area Circumference of cirlce 
Author       : Omkar Jadhav
Date         : 8-March-2022
'''

class Circle:
	PI=3.14
	def __init__(self):
		self.Radius=0.0
		self.Area=0.0
		self.Circumference=0.0

	def Accept(self):
		self.Radius=int(input("Enter the radius:"))

	def CalculateArea(self):
		self.Area=Circle.PI*(self.Radius**2)

	def CalculateCircumference(self):
		self.Circumference=2*Circle.PI*self.Radius

	def Display(self):
		print("Value stored in Radius is:",self.Radius)
		print("Value stored in Area is:",self.Area)
		print("Value stored in Circumference is:",self.Circumference)


def main():
	obj=Circle()
	obj.Accept()
	obj.CalculateArea()
	obj.CalculateCircumference()
	obj.Display()

if __name__=="__main__":
	main()