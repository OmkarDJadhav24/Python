def Check(no):
	for i in range(1,no):
		if(no%i)!=0:
			print(i)

def main():
	print("Enter the number:")
	no=int(input())

	Check(no)

if __name__=="__main__":
	main()