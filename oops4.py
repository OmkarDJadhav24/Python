'''
Program Name : oops1.py
Input        : String Values
Output       : String Values
Description  : It is used to display Name,Author And No of Books 
Author       : Omkar Jadhav
Date         : 8-March-2022
'''

class BookStore:
	NoOfBooks=0
	def __init__(self,Name,Author):
		self.Name=Name
		self.Author=Author
		BookStore.NoOfBooks=1

	def Display(self):
		print("Name of Books:",self.Name)
		print("Name of Author:",self.Author)
		print("Number of Books:",BookStore.NoOfBooks)

def main():
	obj1=BookStore("Linux System Programming","Robert Love")
	obj2=BookStore("C Programming","Dennis Ritchie")
	obj1.Display()
	obj2.Display()

if __name__=="__main__":
	main()