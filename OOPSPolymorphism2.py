# Method Overloading
# It access only last method of overloading

class Parent:
	def __init__(self):
		print("Inside init method")

	
	def Show(self,a,b):
		print("Inside Show with 2 parameters")

	def Show(self,a):
		print("Inside show with one parameter")


def main():
	obj=Parent()
	obj.Show(11)	

if __name__=="__main__":
	main()