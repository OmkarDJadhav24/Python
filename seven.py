def main():
	char=input()
	if char.islower():
		print(char.upper())

	elif char.isupper():
		print(char.lower())

if __name__=="__main__":
	main()