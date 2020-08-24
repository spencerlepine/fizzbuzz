# Fizzbuzz Challenge 8/24/2020

for i in range(101):
	valToPrint = i

	if i > 0:
		if valToPrint % 3 == 0:
			if valToPrint % 5 == 0:
				valToPrint = "FizzBuzz"
				print(valToPrint)
				continue
			valToPrint = "Fizz"
		elif valToPrint % 5 == 0:
			valToPrint = "Buzz"

		print(valToPrint)