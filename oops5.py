'''
Program Name : oops2.py
Input        : String Values
Output       : String Value and Integer Values
Description  : It is used to display Name of Customer Amount And Rate of Interest
Author       : Omkar Jadhav
Date         : 8-March-2022
'''


class BankAccount:
	ROI=10.5
	def __init__(self):
		self.Name=input("Enter the name of Customer:")
		self.Amount=0
		self.Rate=0

	def Deposit(self):
		self.Amount=int(input("Enter the amount for deposite:"))

	def Withdraw(self):
		withdraw=int(input("Enter the amount for withdraw:"))
		self.Amount=self.Amount-withdraw

	def CalculateInterest(self):
		self.Rate=self.Amount/BankAccount.ROI

	def Display(self):
		print("Name of Customer is:",self.Name)
		print("Amount is:",self.Amount)
		print("Rate of Interest is:",self.Rate)

def main():
	obj=BankAccount()
	obj.Deposit()
	obj.Withdraw()
	obj.CalculateInterest()
	obj.Display()

if __name__=="__main__":
	main()