def fun(no):
	if(no%2==0):
		print("This is Even number")
	else:
		print("This is odd number")
def main():
	no=int(input("Enter the number:"))
	fun(no)
if __name__=="__main__":
	main()