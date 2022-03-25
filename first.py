'''
Chef is struggling to pass a certain college course.

The test has a total of N question, each question carries 3 marks for a correct answer and −1 for an incorrect answer. Chef is a risk-averse person so he decided to attempt all the questions. It is known that Chef got X questions correct and the rest of them incorrect. For Chef to pass the course he must score at least P marks.

Will Chef be able to pass the exam or not?
'''
def main():
	T=int(input())

	for i in range(T):
		print("Enter the values of N,X,P:")
		N=int(input())
		X=int(input())
		P=int(input())
		if(X*3-(N-X)*1)>=P:
			print("Pass")
		else:
			print("Fail")

if __name__=="__main__":
	main()