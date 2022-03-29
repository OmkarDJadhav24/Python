def main():
	n=int(input())
	#a=int(input())
	min=3
	sum=0

	for i in range(n):
		a=int(input())
		if(a<min):
			min=a
		sum=sum+a

	minimum=sum-min
	print("Addition:",minimum)

if __name__=="__main__":
	main()