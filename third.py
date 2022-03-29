def main():
	print("Enter the first number:")
	no1=int(input())

	print("Enter the second number:")
	no2=int(input())

	for no in range(no1,no2+1):
		if(no%10) in [2,3,9]:
			print(no)

if __name__=="__main__":
	main()