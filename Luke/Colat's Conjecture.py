def even(x):
	y = x//2
	z = x / 2
	if z == y:
		return True
	else:
		return False
		
steps = 0
mult3s = 0

number = int(input("What number should we start on?"))

while number !=1:
	print(number)
	if even(number):
		number = number // 2
		steps = steps + 1
	else:
		number = number * 3 +1
		steps = steps + 1
		mult3s = mult3s + 1

print(1)
print("This took ", steps, " steps to complete")
print("We ran into ", mult3s, " odd numbers")
	