def Check(no):
	for i in range(no-1,0,-1):
		if(no%i)==0:
			print(i)

def main():
	print("Enter the number:")
	no=int(input())

	Check(no)

if __name__=="__main__":
	main()