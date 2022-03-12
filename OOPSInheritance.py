# Inheritance
class Parent:
	def __init__(self):
		self.no1=10

	def Fun(self):
		print("Inside Fun")

class Child(Parent):
	def __init__(self):
		self.no2=20
		Parent.Fun(self)

	def Gun(self):
		print("Inside Gun")

def main():
	obj=Child()
	obj.Fun()

if __name__=="__main__":
	main()