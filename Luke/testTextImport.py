f = open("./PrimeNumbersList.txt")
lines = f.readlines()
lines = list(map(int, lines))


number = 1

while number != 9999:
	number = int(input("what prime do you want?"))
	print(lines[number])

	