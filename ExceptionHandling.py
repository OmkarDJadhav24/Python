def Division(no1,no2):
	ans=0
	ans=no1/no2
	return ans

def main():
	print("Enter the first number:")
	no1=int(input())

	print("Enter the second number:")
	no2=int(input())

	try:
		ret=Division(no1,no2)
		print("Division is:",ret)
	except Exception as E:
		print("Exception is:",E)

if __name__=="__main__":
	main()