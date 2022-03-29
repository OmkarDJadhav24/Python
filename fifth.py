def main():
	strr="Www.HackerRank.com"

	for char in strr:
		if char.islower()==True:
			print(char.upper(),end="")
		elif char.isupper()==True:
			print(char.lower(),end="")
		else:
			print(char,end="")

if __name__=="__main__":
	main()