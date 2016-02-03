#The following three lines import a list of 1000 prime numbers from the file PrimeNumbersList.txt and store it in the list primes[]
f = open("./PrimeNumbersList.txt")
primes = f.readlines()
primes = list(map(int, primes))

def primefac(number):
	index = 0
	while number >= primes[index]:
		dontMoveOn = True
		while dontMoveOn:
			if number/primes[index] == number//primes[index]:
				number = number / primes[index]
				print(primes[index])
			else:
				dontMoveOn = False
				index = index + 1
	if number != 1:
		print(number)
		
testnum = int(input("what do you want the prime factorization of?"))
primefac(testnum)