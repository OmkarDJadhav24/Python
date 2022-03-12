def Substraction(no1,no2):
	ans=0
	ans=no1-no2
	return ans
def SmartSub(fun_name):
	def Inner_fun(no1,no2):
		if(no1<no2):
			no1,no2=no2,no1
		return fun_name(no1,no2)
	return Inner_fun
	
Substraction=SmartSub(Substraction)

def main():
	print("Enter the first number:")
	no1=int(input())

	print("Enter the second number:")
	no2=int(input())

	ret=Substraction(no1,no2)
	print("Substraction is:",ret)

if __name__=="__main__":
	main()