# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

def find_factors(n):
	factors = []
	i = 2
	while(i <= n // 2):				
		if (n % i == 0):						# if n divides nicely (no remainder)
			factors.extend(find_factors(n / i))
			factors.extend(find_factors(i))
			return factors
		i += 1

	# must be prime (no factors)
	factors.append(n) 
	return factors

from math import sqrt
def elegant():
	n = 1	# looking for the nth prime
	i = 2	# start trying at 2
	sum = 0

	factors = []

	while(i < 2000000):
		isPrime = True

		root = sqrt(i)
		# test against factors list 
		for f in factors:
			if (f > root):	# only need to test up to square root
				break

			if ( i % f == 0):
				isPrime = False
				break
		
		if (isPrime):
			sum += i
			factors.append(i)
			n += 1

		i += 1
	print "sum=", sum

elegant()