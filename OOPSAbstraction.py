# Abstraction

class Arithmatic:
	value=11
	def __init__(self,no1,no2):
		self.no1=no1
		self.__no2=no2

	def Addition(self):
		ans=0
		ans=self.no1+self.no2
		return ans
	def Substraction(self):
		ans=0
		ans=self.no1-self.no2
		return ans
	def Display(self):
		print(self.no1)
		print(self.no2)

def main():
	obj=Arithmatic(20,10)
	ret1=obj.Addition()
	ret2=obj.Substraction()
	obj.Display()
	print(ret1)
	print(ret2)
	print(obj.no1)
	print(obj.__no2)
if __name__=="__main__":
	main()