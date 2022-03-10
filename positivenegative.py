
def main():
	print("Enter the number to check positive or negative")
	no=int(input())

	if(no>0):
		print("this is positive number")
	elif(no<0):
		print("This is negative number")
	else:
		print("The number is Zero")
		
if __name__=="__main__":
	main()