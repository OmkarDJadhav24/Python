# Docstring(Documentation string)

def Display_Doc():
	'''
	This statements contains Documentation string
	the Aim of this fun  is to display the comments
	which represents the documentation string  
	'''
	print("Hello")

	print("Docstring Display using __doc__")
	print(Display_Doc.__doc__)

	print("Doc string display using help keyword")
	help(Display_Doc)
	
def main():
	Display_Doc()
if __name__=="__main__":
	main()