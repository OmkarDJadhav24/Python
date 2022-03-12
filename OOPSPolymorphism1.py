# Method Overriding/Function Overriding

class Parent:
	def __init__(self):
		print("Inside init of parent")

	def Display(self):
		print("Inside Display of parent")

	def Show(self):
		print("Inside Show")

class Child(Parent):
	def __init__(self):
		print("Inside init of child")

	def Display(self):
		print("Inside Display of child")

	def View(self):
		print("Inside View")

def main():
	pobj=Parent()
	cobj=Child()
	cobj.Display()
	pobj.Display()
	cobj.Show()
	cobj.View()

if __name__=="__main__":
	main()