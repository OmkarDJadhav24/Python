def Check(char):
	if char not in ['a','e','i','o','u']:
		return False
	else:
		return True

def main():
	Result=False
	print("Enter the character:")
	char=input()

	Result=Check(char)
	print(Result)

if __name__=="__main__":
	main()