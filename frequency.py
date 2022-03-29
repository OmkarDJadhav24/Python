def Check(no):
	N=0
	cnt=0
	while(no>0):
		N=no%10
		if(N==2):
			cnt=cnt+1
		no=no//10

	return cnt

def main():
	Result=0
	print("Enter the number:")
	no=int(input())

	Result=Check(no)
	print("Frequency of 2 is: ",Result)

if __name__=="__main__":
	main()