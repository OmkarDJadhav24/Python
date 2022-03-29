
def Check(no):
	list=[]
	for i in range(1,no):
		if(no%i)==0:
			if(i%2)==0:
				list.append(i)

	print(list)

def main():
	no=int(input("Enter the number:"))

	Check(no)

if __name__=="__main__":
	main()