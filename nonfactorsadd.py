def Check(no):
	icnt=0
	for i in range(1,no):
		if(no%i) !=0:
			icnt=icnt+i

	return icnt

def main():
	no=int(input("Enter the number:"))
	Result=0

	Result=Check(no)
	print("Addition of non factors:",Result)

if __name__=="__main__":
	main()