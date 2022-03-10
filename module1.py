'''
Program Name : module1.py
Input        : two Integers
Output       : Integer
Description  : It is used to perform addition using scheduler
Author       : Omkar Jadhav
Date         : 7-March-2022
'''


from module2 import *
import datetime
import schedule
import time

def Add(no1,no2):
	result1=Addition(no1,no2)
	print("Addition is:",result1)
def Sub(no1,no2):
	result2=Substraction(no1,no2)
	print("Substraction is:",result2)
def Mult(no1,no2):
	result3=Multiplication(no1,no2)
	print("Multiplication is:",result3)
def Div(no1,no2):
	result4=Division(no1,no2)
	print("Division is:",result4)


def main():
	starttime=datetime.datetime.now()
	print(starttime)
	print("Enter the first number:")
	no1=int(input())

	print("Enter the second number:")
	no2=int(input())

	schedule.every(1).minute.do(Add,no1,no2)
	schedule.every(2).minutes.do(Sub,no1,no2)
	schedule.every(3).minutes.do(Mult,no1,no2)
	schedule.every(4).minutes.do(Div,no1,no2)

	while(True):
		schedule.run_pending()
		time.sleep(2)


	print('Addition is:{},Substraction is:{},Multiplication is:{},Division is:{}'.format(result1,result2,result3,result4))
	endtime=datetime.datetime.now()
	print(endtime)

if __name__=="__main__":
	main()