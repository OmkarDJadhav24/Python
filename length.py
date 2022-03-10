def lengt(name):
	count=0
	for char in name:
		count=count+1
	
	return count

def main():
	print("Enter the string")
	name=input()

	#length=len(name)
	length=lengt(name)
	print(length)
if __name__=="__main__":
	main()