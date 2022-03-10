'''
Program Name : oops3.py
Input        : Integer
Output       : Boolean Value and Integer Values
Description  : It is used to check Number is prime Perfect or not and Display Addition of its Factors
Author       : Omkar Jadhav
Date         : 8-March-2022
'''


class Arithmetic:
	def __init__(self,value):
		self.value=value
		self.data=[]

	def chkprime(self):
		flag=True
		for i in range(2,self.value):
			if(self.value%i)==0:
				flag=False
		if(flag):
			return "True"
		else:
			return "False"

	def chkperfect(self):
		list=[]
		ans=0
		for i in range(1,self.value):
			if(self.value>0):
				if(self.value%i)==0:
					list.append(i)
		for no in list:
			ans=ans+no

		if(ans==self.value):
			return True
		else:
			return False

	def factors(self):
		
		for i in range(1,self.value+1):
			if(self.value>1):
				if(self.value%i)==0:
					self.data.append(i)
		return self.data

	def SumFactor(self):
		ans=0
		for no in self.data:
			ans=ans+no

		return ans

def main():
	print("Enter the Number:")
	no=int(input())

	obj=Arithmetic(no)
	result1=obj.chkprime()
	result2=obj.chkperfect()
	result3=obj.factors()
	result4=obj.SumFactor()

	print("Prime:",result1)
	print("Perfect:",result2)
	print("Factors:",result3)
	print("Sum Of Factors:",result4)

if __name__=="__main__":
	main()