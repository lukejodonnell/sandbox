running = True

#The following four lines import a list of 1000 prime numbers from the file PrimeNumbersList.txt and store it in the list primes[]
f = open("./PrimeNumbersList.txt")
primes = f.readlines()
primes = list(map(int, primes))
f.close()

def primefac(number):
	index = 0
	if number < 0:
		number = -number
		print(-1)
	if number == 1:
		print("1 (kinda, 1 is not a prime number)")
	if number == 0:
		print("0 is just weird man, it has every factor")
	if number != 1 and number != 0:
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
			print("sorry, couldn't finish the problem, here is the remainder")
			print(number)
		
while running:
	testnum = int(input("what do you want the prime factorization of? "))
	primefac(testnum)
	if input("Do you want to factorize another number? y/n ") != "y":
		running = False
		print("okay goodbye!")