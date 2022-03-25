'''
Team RCB has earned X points in the games it has played so far in this year's IPL. To qualify for the playoffs they must earn at least a total of Y points. They currently have Z games left, in each game they earn 2 points for a win, 1 point for a draw, and no points for a loss.

Is it possible for RCB to qualify for the playoffs this year?
'''

def main():
	print("Enter the test cases:")
	T=int(input())

	for i in range(T):
		print("Enter the values of X,Y,Z:")
		X=int(input())
		Y=int(input())
		Z=int(input())

		if(X+Z*2)>=Y:
			print("RCB will Win")
		else:
			print("RCB will Lose")
			
if __name__=="__main__":
	main()