def Check(no):
	N=0
	list=[]
	while(no>0):
		N=no%10
		list.append(N)
		no=no//10

	print(list)
	for i in range(len(list)-1,-1,-1):
		print(list[i])

def main():
	print("Enter the number:")
	no=int(input())

	Check(no)

if __name__=="__main__":
	main()