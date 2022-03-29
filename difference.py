def Check(no):
	factor=0
	nonfactor=0
	diff=0
	for i in range(1,no):
		if(no%i)==0:
			factor=factor+i
		else:
			nonfactor=nonfactor+i

	diff=factor-nonfactor

	return diff

def main():
	no=int(input("Enter the number:"))
	Result=0

	Result=Check(no)
	print(Result)

if __name__=="__main__":
	main()