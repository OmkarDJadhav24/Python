def Check(no):
	if (no%10)==0:
		print("It contains Zero")
	else:
		print("There is no zero")

def main():
	no=int(input("Enter the number:"))

	Check(no)

if __name__=="__main__":
	main()